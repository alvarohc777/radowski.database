CREATE TABLE "poem" (
  "id" serial PRIMARY KEY,
  "name" varchar(35) NOT NULL,
  "title" varchar(35) NOT NULL,
  "cover_url" varchar(100),
  "is_active" bool NOT NULL DEFAULT 'true',
  "created_at" timestamp without time zone,
  "updated_at" timestamp without time zone
);

CREATE TABLE "language" (
  "id" int PRIMARY KEY NOT NULL,
  "name" varchar(35) NOT NULL,
  "original_name" varchar(35) NOT NULL
);

CREATE TABLE "content" (
  "id" serial PRIMARY KEY,
  "poem_id" int,
  "name" varchar(35) NOT NULL,
  "title" varchar(35) NOT NULL,
  "body" varchar(2500) NOT NULL,
  "cover_url" varchar(100) NOT NULL,
  "ig_url" varchar(100),
  "language_id" int NOT NULL,
  "created_at" timestamp without time zone,
  "updated_at" timestamp without time zone
);

CREATE TABLE "content_image" (
  "id" serial PRIMARY KEY,
  "content_id" int NOT NULL,
  "pages" int NOT NULL,
  "img_url" varchar(100),
  "created_at" timestamp without time zone,
  "updated_at" timestamp without time zone
);

CREATE TABLE "book_content" (
  "id" serial PRIMARY KEY,
  "book_id" int NOT NULL,
  "content_id" int NOT NULL
);

CREATE TABLE "book" (
  "id" serial PRIMARY KEY,
  "name" varchar(35) NOT NULL,
  "title" varchar(35) NOT NULL,
  "pdf_url" varchar(100) NOT NULL,
  "cover_url" varchar(100) NOT NULL,
  "created_at" timestamp without time zone,
  "updated_at" timestamp without time zone
);

ALTER TABLE "book_content" ADD FOREIGN KEY ("book_id") REFERENCES "book" ("id");
ALTER TABLE "book_content" ADD FOREIGN KEY ("content_id") REFERENCES "content" ("id");

ALTER TABLE "content" ADD FOREIGN KEY ("language_id") REFERENCES "language" ("id");
ALTER TABLE "content" ADD FOREIGN KEY ("poem_id") REFERENCES "poem" ("id");
ALTER TABLE "content_image" ADD FOREIGN KEY ("content_id") REFERENCES "content" ("id");

ALTER TABLE "book_content" ADD CONSTRAINT book_content_alt_key 
UNIQUE (book_id, content_id)