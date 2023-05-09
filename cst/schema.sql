DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS corpus;
DROP TABLE IF EXISTS corpus_query;
DROP TABLE IF EXISTS document;
DROP TABLE IF EXISTS document_properties;
DROP TABLE IF EXISTS document_has_property;
DROP TABLE IF EXISTS document_in_corpus;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE corpus (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  description TEXT,
  user_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES user(id)
);

CREATE TABLE document_in_corpus (
  corpus_id INTEGER NOT NULL,
  document_id INTEGER NOT NULL,
  FOREIGN KEY (corpus_id) REFERENCES corpus(id),
  FOREIGN KEY (document_id) REFERENCES document(id)
);

CREATE TABLE document (
  id TEXT PRIMARY KEY
);

CREATE TABLE document_properties (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  property_group TEXT
  );

CREATE TABLE document_has_property (
  document_id TEXT NOT NULL,
  property_id INTEGER NOT NULL,
  property_value TEXT,
  FOREIGN KEY (document_id) REFERENCES document(id),
  FOREIGN KEY (property_id) REFERENCES document_properties(id)
);

CREATE TABLE corpus_query (
  corpus_id INTEGER NOT NULL,
  filter_item,
  filter_value,
  FOREIGN KEY (corpus_id) REFERENCES corpus(id)
);