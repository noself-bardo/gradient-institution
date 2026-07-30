grant usage on schema gradient to authenticated;

grant select on all tables in schema gradient to authenticated;

alter default privileges in schema gradient grant select on tables to authenticated;

do $$
declare
  table_name text;
  policy_name text;
begin
  foreach table_name in array array[
    'departments',
    'standards',
    'collections',
    'publications',
    'artifacts',
    'prompt_packets',
    'image_generations',
    'qc_reports',
    'layouts',
    'print_packages',
    'archive_records',
    'automation_jobs',
    'events',
    'sync_records',
    'platform_assets'
  ]
  loop
    policy_name := 'authenticated_read_' || table_name;
    execute format('drop policy if exists %I on gradient.%I', policy_name, table_name);
    execute format(
      'create policy %I on gradient.%I for select to authenticated using (true)',
      policy_name,
      table_name
    );
  end loop;
end;
$$;
