CREATE TABLE files_list(
      id serial NOT NULL,
      path character varying,
      insert_time timestamp without time zone,
      inserted boolean DEFAULT false,
      lock_time timestamp without time zone,
      locked boolean DEFAULT false,
      CONSTRAINT files_list_pkey PRIMARY KEY (id),
      CONSTRAINT files_list_path_key UNIQUE (path),
      CONSTRAINT path_uniq UNIQUE (path)
);
