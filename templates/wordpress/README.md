# WordPress execution templates

Worked examples of the two machine-readable files on a WordPress site, plus the plugin
filters that produce them. Read [../../search/13-schema-and-technical-wiring.md](../../search/13-schema-and-technical-wiring.md)
first for the method; this folder is only the WordPress mechanics.

| File | What it is |
|---|---|
| [llms.txt.example](llms.txt.example) | A filled-in `llms.txt` for a fictional WordPress site, plus the two ways to serve it (static file at root, or a rewrite rule that generates it) |
| [sitemap.xml.example](sitemap.xml.example) | A correct sitemap index and child sitemap, with the exclusion filters for core, Yoast and Rank Math, and the list of URLs WordPress adds that should not be there |

The blank, stack-agnostic versions live one level up: [../llms.txt.example](../llms.txt.example)
and [../robots.txt.example](../robots.txt.example). The Next.js equivalents are in
[../nextjs/](../nextjs/README.md).

## The three WordPress traps

**1. Two sitemap generators running at once.** WordPress core has served `/wp-sitemap.xml`
since 5.5. Yoast and Rank Math serve `/sitemap_index.xml` and disable core automatically —
but a half-configured site can end up with both live, and Search Console indexed against the
one you did not prune. Check all three URLs before you submit anything:

```bash
curl -sI https://example.com/wp-sitemap.xml
curl -sI https://example.com/sitemap_index.xml
curl -s  https://example.com/robots.txt | grep -i sitemap
```

**2. `robots.txt` is virtual.** There is usually no file on disk, so an FTP edit does
nothing. WordPress generates it on request, and the `Sitemap:` line it emits often points at
a staging host or the wrong protocol after a migration. Either edit it in your SEO plugin's
file editor, or filter it:

```php
add_filter('robots_txt', function ($output, $public) {
    if (!$public) { return $output; }             // leave a non-public site alone
    $lines = [
        'User-agent: *',
        'Disallow: /wp-admin/',
        'Allow: /wp-admin/admin-ajax.php',
        'Disallow: /?s=',
        'Disallow: /search/',
        '',
        // Answer engines — allow the ones you want quoting you.
        'User-agent: OAI-SearchBot',   'Allow: /',
        'User-agent: PerplexityBot',   'Allow: /',
        'User-agent: ClaudeBot',       'Allow: /',
        '',
        'Sitemap: https://example.com/sitemap_index.xml',
    ];
    return implode("\n", $lines) . "\n";
}, 10, 2);
```

Decide separately whether to allow training crawlers (`GPTBot`, `Google-Extended`, `CCBot`).
Blocking them does not remove you from AI answers that use live search; allowing them does
not guarantee citation. Make it a deliberate choice, not a default you inherited.

**3. Anything that is noindex must also be out of the sitemap.** In Yoast and Rank Math,
setting a post type or taxonomy to "not shown in search results" does both at once — use the
UI rather than a filter wherever it exists, so the two can never disagree.

## Apply it

- [ ] Only one sitemap generator is live, and the index URL is the one submitted to Search Console and Bing.
- [ ] Attachment pages, author archives, date archives, pagination, search URLs and feeds are all excluded.
- [ ] Every URL in the sitemap returns 200, is self-canonical, and is not noindex.
- [ ] `lastmod` reflects the real modified date; nothing was touched just to look fresh.
- [ ] `robots.txt` is served through the plugin or the `robots_txt` filter, and its `Sitemap:` line points at the live host.
- [ ] The AI-crawler decision was made deliberately and written down, not inherited from a default.
- [ ] `llms.txt` returns 200 as `text/plain`, and is not intercepted by a cache or security plugin.
- [ ] `llms.txt` links only public, indexable, pretty-permalink URLs — no `/wp-json/`, `/?p=`, feeds or attachments.
- [ ] The entity paragraph in `llms.txt` is byte-identical to the one in the schema and the About page.

## Related

- [../../search/13-schema-and-technical-wiring.md](../../search/13-schema-and-technical-wiring.md) — the method these files execute
- [../../search/12-geo-ai-search.md](../../search/12-geo-ai-search.md) — why `llms.txt` and entity consistency matter
- [../../search/11-seo-fundamentals.md](../../search/11-seo-fundamentals.md) — indexing, canonicals and crawl budget
- [../llms.txt.example](../llms.txt.example) · [../robots.txt.example](../robots.txt.example) — the blank, stack-agnostic versions
- [../page-brief.md](../page-brief.md) — the per-page spec that feeds both files
- [../../skills/growth-search.skill.md](../../skills/growth-search.skill.md) — the agent procedure that enforces all of this
