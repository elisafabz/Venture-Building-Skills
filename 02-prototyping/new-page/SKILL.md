---
name: new-page
description: Scaffold a new page with route, lazy-loading, SEO meta, and mobile-first layout following project conventions
argument-hint: [page-name]
model: opus
effort: medium
---

# Create New Page

Scaffold a new page named `$ARGUMENTS` following the project's existing patterns.

## Steps

1. **Read the project's router setup** — find how routes are defined (React Router, file-based, etc.)
2. **Read existing pages** — match the pattern (lazy-loading, layout wrappers, etc.)
3. **Create the page component** at `src/pages/$ARGUMENTS.tsx`
4. **Register the route** in the router config
5. **Add lazy-loading** if the project uses it

## Page Template

```typescript
import { useEffect } from "react";

const PAGE_TITLE = "$ARGUMENTS";
const PAGE_DESCRIPTION = "TODO: add description";

const $ARGUMENTS = () => {
  useEffect(() => {
    document.title = PAGE_TITLE;
    document.querySelector('meta[name="description"]')
      ?.setAttribute("content", PAGE_DESCRIPTION);
  }, []);

  return (
    <div className="min-h-screen">
      {/* Mobile-first: base styles for mobile, md: for desktop */}
      <div className="container mx-auto px-4 py-8 md:py-16">
        <h1 className="text-2xl md:text-4xl font-bold">
          {PAGE_TITLE}
        </h1>
      </div>
    </div>
  );
};

export default $ARGUMENTS;
```

## Route Registration (React Router)

```typescript
// Lazy-loaded import
const $ARGUMENTS = lazy(() => import("./pages/$ARGUMENTS"));

// In routes array
{ path: "/$ARGUMENTS", element: <$ARGUMENTS /> }
```

## Rules

- **Match existing patterns** — if pages use a layout wrapper, use it
- **Mobile-first** — base styles for mobile, `md:` breakpoint for desktop
- **Lazy-load** unless it's a critical first-paint page (like Index/Home)
- **SEO** — set document.title and meta description
- **Use project fonts/colors** from the design system
- **TypeScript** — proper types, no `any`
- **No unnecessary deps** — use what's already in the project
