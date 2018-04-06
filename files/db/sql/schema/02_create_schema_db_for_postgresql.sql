
-- Qua 04 Abr 2018 20:00:47 -03

-- -----------------------------------------------------
-- Table user_
-- -----------------------------------------------------
DROP TABLE IF EXISTS user_ CASCADE ;

CREATE TABLE IF NOT EXISTS user_ (
  id SERIAL ,
  email TEXT NOT NULL,
  password VARCHAR(255) NOT NULL,
  username TEXT NOT NULL,
  name TEXT NULL,
  is_email_valid BOOLEAN NOT NULL DEFAULT FALSE,
  terms_agreed BOOLEAN NOT NULL DEFAULT FALSE,
  created_at TIMESTAMP NOT NULL,
  visible BOOLEAN NOT NULL DEFAULT TRUE,
  PRIMARY KEY (id)
);


-- -----------------------------------------------------
-- Table theme
-- -----------------------------------------------------
DROP TABLE IF EXISTS theme CASCADE ;

CREATE TABLE IF NOT EXISTS theme (
  id SERIAL ,
  name VARCHAR(45) NULL,
  fk_parent_id INT NULL,
  fk_user_id INT NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT fk_theme_theme1
    FOREIGN KEY (fk_parent_id)
    REFERENCES theme (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT fk_theme_user_1
    FOREIGN KEY (fk_user_id)
    REFERENCES user_ (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);


-- -----------------------------------------------------
-- Table project
-- -----------------------------------------------------
DROP TABLE IF EXISTS project CASCADE ;

CREATE TABLE IF NOT EXISTS project (
  id SERIAL ,
  name TEXT NOT NULL,
  description TEXT NULL,
  created_at TIMESTAMP NOT NULL,
  removed_at TIMESTAMP NULL,
  visible BOOLEAN NOT NULL DEFAULT TRUE,
  fk_user_id INT NOT NULL,
  fk_theme_id INT NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT fk_project_user_1
    FOREIGN KEY (fk_user_id)
    REFERENCES user_ (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT fk_project_theme1
    FOREIGN KEY (fk_theme_id)
    REFERENCES theme (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);


-- -----------------------------------------------------
-- Table layer
-- -----------------------------------------------------
DROP TABLE IF EXISTS layer CASCADE ;

CREATE TABLE IF NOT EXISTS layer (
  id SERIAL ,
  table_name TEXT NOT NULL UNIQUE,
  name TEXT NOT NULL,
  description TEXT NULL,
  source TEXT NULL,
  created_at TIMESTAMP NOT NULL,
  removed_at TIMESTAMP NULL,
  visible BOOLEAN NOT NULL DEFAULT TRUE,
  fk_project_id INT NOT NULL,
  fk_user_id INT NOT NULL,
  fk_theme_id INT NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT fk_project_user1
    FOREIGN KEY (fk_user_id)
    REFERENCES user_ (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT fk_layer_project1
    FOREIGN KEY (fk_project_id)
    REFERENCES project (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT fk_layer_theme1
    FOREIGN KEY (fk_theme_id)
    REFERENCES theme (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);


-- -----------------------------------------------------
-- Table changeset
-- -----------------------------------------------------
DROP TABLE IF EXISTS changeset CASCADE ;

CREATE TABLE IF NOT EXISTS changeset (
  id SERIAL ,
  description VARCHAR(45) NULL,
  created_at TIMESTAMP NOT NULL,
  closed_at TIMESTAMP NULL,
  fk_user_id INT NOT NULL,
  fk_layer_id INT NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT fk_tb_project_tb_user1
    FOREIGN KEY (fk_user_id)
    REFERENCES user_ (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT fk_change_set_project1
    FOREIGN KEY (fk_layer_id)
    REFERENCES layer (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);


-- -----------------------------------------------------
-- Table version_feature
-- -----------------------------------------------------
DROP TABLE IF EXISTS version_feature CASCADE ;

CREATE TABLE IF NOT EXISTS version_feature (
  id SERIAL ,
  geom GEOMETRY(GEOMETRYCOLLECTION, 4326) NOT NULL,
  start_date TIMESTAMP NULL,
  end_date TIMESTAMP NULL,
  file TEXT NULL,
  version INT NOT NULL DEFAULT 1,
  visible BOOLEAN NOT NULL DEFAULT TRUE,
  fk_changeset_id INT NOT NULL,
  PRIMARY KEY (id, version),
  CONSTRAINT fk_tb_contribution_tb_project1
    FOREIGN KEY (fk_changeset_id)
    REFERENCES changeset (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);


-- -----------------------------------------------------
-- Table auth
-- -----------------------------------------------------
DROP TABLE IF EXISTS auth CASCADE ;

CREATE TABLE IF NOT EXISTS auth (
  id SERIAL ,
  is_admin BOOLEAN NOT NULL DEFAULT FALSE,
  is_moderator BOOLEAN NOT NULL DEFAULT FALSE,
  fk_user_id INT NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT fk_auth_user1
    FOREIGN KEY (fk_user_id)
    REFERENCES user_ (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);


-- -----------------------------------------------------
-- Table user_project
-- -----------------------------------------------------
DROP TABLE IF EXISTS user_project CASCADE ;

CREATE TABLE IF NOT EXISTS user_project (
  fk_user_id INT NOT NULL,
  fk_project_id INT NOT NULL,
  added_at TIMESTAMP NULL,
  PRIMARY KEY (fk_user_id, fk_project_id),
  CONSTRAINT fk_project_subscriber_user1
    FOREIGN KEY (fk_user_id)
    REFERENCES user_ (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT fk_project_subscriber_project1
    FOREIGN KEY (fk_project_id)
    REFERENCES project (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);


-- -----------------------------------------------------
-- Table feature
-- -----------------------------------------------------
DROP TABLE IF EXISTS feature CASCADE ;

CREATE TABLE IF NOT EXISTS feature (
  id SERIAL ,
  geom GEOMETRY(GEOMETRYCOLLECTION, 4326) NOT NULL,
  start_date TIMESTAMP NULL,
  end_date TIMESTAMP NULL,
  file TEXT NULL,
  version INT NOT NULL DEFAULT 1,
  fk_changeset_id INT NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT fk_tb_contribution_tb_project10
    FOREIGN KEY (fk_changeset_id)
    REFERENCES changeset (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);


-- -----------------------------------------------------
-- Table review
-- -----------------------------------------------------
DROP TABLE IF EXISTS review CASCADE ;

CREATE TABLE IF NOT EXISTS review (
  id SERIAL ,
  description TEXT NOT NULL,
  create_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP NULL,
  closed_at TIMESTAMP NULL,
  fk_user_id INT NOT NULL,
  fk_layer_id INT NOT NULL,
  fk_parent_id INT NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT fk_review_layer1
    FOREIGN KEY (fk_layer_id)
    REFERENCES layer (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT fk_review_user_1
    FOREIGN KEY (fk_user_id)
    REFERENCES user_ (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT fk_layer_comment_layer_comment1
    FOREIGN KEY (fk_parent_id)
    REFERENCES review (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);


-- -----------------------------------------------------
-- Table notification
-- -----------------------------------------------------
DROP TABLE IF EXISTS notification CASCADE ;

CREATE TABLE IF NOT EXISTS notification (
  id SERIAL ,
  name TEXT NOT NULL,
  description TEXT NOT NULL,
  icon TEXT NULL,
  created_at TIMESTAMP NOT NULL,
  fk_project_id INT NULL,
  fk_layer_id INT NULL,
  fk_review_id INT NULL,
  PRIMARY KEY (id),
  CONSTRAINT fk_notification_layer1
    FOREIGN KEY (fk_layer_id)
    REFERENCES layer (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT fk_notification_layer_review1
    FOREIGN KEY (fk_review_id)
    REFERENCES review (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT fk_notification_project1
    FOREIGN KEY (fk_project_id)
    REFERENCES project (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);


-- -----------------------------------------------------
-- Table user_notification
-- -----------------------------------------------------
DROP TABLE IF EXISTS user_notification CASCADE ;

CREATE TABLE IF NOT EXISTS user_notification (
  fk_user_id INT NOT NULL,
  fk_notification_id INT NOT NULL,
  CONSTRAINT fk_user_notification_user_1
    FOREIGN KEY (fk_user_id)
    REFERENCES user_ (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT fk_user_notification_notification1
    FOREIGN KEY (fk_notification_id)
    REFERENCES notification (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);


-- -----------------------------------------------------
-- Table bulk_import
-- -----------------------------------------------------
DROP TABLE IF EXISTS bulk_import CASCADE ;

CREATE TABLE IF NOT EXISTS bulk_import (
  id SERIAL ,
  file BYTEA NULL,
  description TEXT NULL,
  accepted BOOLEAN NULL,
  created_at VARCHAR(45) NULL,
  accepted_at VARCHAR(45) NULL,
  fk_user_id INT NOT NULL,
  fk_layer_id INT NOT NULL,
  fk_user_id_moderator INT NULL,
  PRIMARY KEY (id),
  CONSTRAINT fk_bulk_import_user_1
    FOREIGN KEY (fk_user_id)
    REFERENCES user_ (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT fk_bulk_import_layer1
    FOREIGN KEY (fk_layer_id)
    REFERENCES layer (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT fk_bulk_import_user_2
    FOREIGN KEY (fk_user_id_moderator)
    REFERENCES user_ (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);
