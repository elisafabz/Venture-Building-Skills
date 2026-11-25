---
name: db-migration
description: Generate a Supabase database migration with table, RLS policies, triggers, and indexes
argument-hint: [table-name]
model: sonnet
effort: medium
---

# Create Database Migration

Generate a Supabase SQL migration for table `$ARGUMENTS`.

## Steps

1. **Read existing migrations** in `supabase/migrations/` to match naming and patterns
2. **Read SCHEMA.md** if it exists for context on existing tables
3. **Create the migration file** at `supabase/migrations/{timestamp}_create_$ARGUMENTS.sql`
4. **Update SCHEMA.md** with the new table documentation

## Migration Template

```sql
-- Create $ARGUMENTS table
CREATE TABLE IF NOT EXISTS public.$ARGUMENTS (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  -- TODO: add columns based on requirements
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- Enable RLS
ALTER TABLE public.$ARGUMENTS ENABLE ROW LEVEL SECURITY;

-- RLS Policies (keep minimal)
CREATE POLICY "Users can read own $ARGUMENTS"
  ON public.$ARGUMENTS
  FOR SELECT
  USING (auth.uid() = user_id);

CREATE POLICY "Users can insert own $ARGUMENTS"
  ON public.$ARGUMENTS
  FOR INSERT
  WITH CHECK (auth.uid() = user_id);

-- Auto-update updated_at
CREATE TRIGGER trg_$ARGUMENTS_updated_at
  BEFORE UPDATE ON public.$ARGUMENTS
  FOR EACH ROW
  EXECUTE FUNCTION update_updated_at_column();

-- Indexes for common queries
CREATE INDEX idx_$ARGUMENTS_user_id ON public.$ARGUMENTS(user_id);
CREATE INDEX idx_$ARGUMENTS_created_at ON public.$ARGUMENTS(created_at);
```

## Rules (from SECURITY_RULES.md)

- **RLS always enabled** — no exceptions
- **Policies as simple as possible** — Principle of Least Privilege
- **Never `USING (true)`** — that grants access to everything
- **Always add `updated_at` trigger** if the table has an `updated_at` column
- **Index FK columns** and columns used in WHERE clauses
- **Use `gen_random_uuid()`** for primary keys, not serial/auto-increment
- **Timestamps always TIMESTAMPTZ** — never plain TIMESTAMP
- **CASCADE on FKs** where appropriate (delete parent → delete children)

## Naming Conventions

- Table names: `snake_case`, plural (`user_events`, not `userEvent`)
- Column names: `snake_case`
- Policies: descriptive English (`"Users can read own orders"`)
- Triggers: `trg_{table}_{action}`
- Indexes: `idx_{table}_{column}`
- Migration files: `{YYYYMMDDHHMMSS}_create_{table}.sql`

## After creating

- Run `supabase db reset` locally to apply
- Verify RLS with: `supabase db test`
- Update SCHEMA.md with the new table documentation
- Generate fresh TypeScript types: `supabase gen types typescript --local > src/integrations/supabase/types.ts`
