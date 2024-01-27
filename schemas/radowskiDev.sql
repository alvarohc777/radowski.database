CREATE TABLE "poem" (
  "id" serial PRIMARY KEY ,
  "name" varchar(35) NOT NULL,
  "title" varchar(35) NOT NULL,
  "cover_url" varchar(100),
  "is_active" boolean NOT NULL DEFAULT true,
  "created_at" timestamp without time zone,
  "updated_at" timestamp without time zone
);

CREATE TABLE "language" (
  "id" int PRIMARY KEY NOT NULL,
  "name" varchar(35) NOT NULL
);

CREATE TABLE "content" (
  "id" serial PRIMARY KEY,
  "name" varchar(35) NOT NULL,
  "title" varchar(35) NOT NULL,
  "body" varchar(2500) NOT NULL,
  "pages" int NOT NULL DEFAULT 1,
  "cover_url" varchar(100) NOT NULL,
  "img_url" varchar(100),
  "ig_url" varchar(100),
  "created_at" timestamp without time zone,
  "updated_at" timestamp without time zone
);

CREATE TABLE "poem_content_language" (
  "id" serial PRIMARY KEY,
  "poem_id" int NOT NULL,
  "content_id" int NOT NULL,
  "language_id" int NOT NULL
);

CREATE TABLE "poem_book_language" (
  "id" serial PRIMARY KEY,
  "poem_id" int NOT NULL,
  "book_id" int NOT NULL,
  "language_id" int NOT NULL
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

ALTER TABLE "poem_content_language" ADD FOREIGN KEY ("poem_id") REFERENCES "poem" ("id");
ALTER TABLE "poem_content_language" ADD FOREIGN KEY ("content_id") REFERENCES "content" ("id");
ALTER TABLE "poem_content_language" ADD FOREIGN KEY ("language_id") REFERENCES "language" ("id");

ALTER TABLE "poem_book_language" ADD FOREIGN KEY ("language_id") REFERENCES "language" ("id");
ALTER TABLE "poem_book_language" ADD FOREIGN KEY ("poem_id") REFERENCES "poem" ("id");
ALTER TABLE "poem_book_language" ADD FOREIGN KEY ("book_id") REFERENCES "book" ("id");

ALTER TABLE "poem_book_language" ADD CONSTRAINT book_alt_key 
UNIQUE (book_id, poem_id, language_id)

