SELECT * FROM api_categories
-- Category
INSERT INTO `django`.`api_categories` (`category_name`, `category_description`, `category_status`, `created_at`, `updated_at`)
VALUES ('Shooter games', 'shooter games (or simply shooters)', 0, '2024-03-21 16:20:25', '2024-03-21 16:20:26');
INSERT INTO `django`.`api_categories` (`category_name`, `category_description`, `category_status`, `created_at`, `updated_at`)
VALUES ('Fighting games', 'Fighting games center around close-ranged combat', 0, '2024-03-21 16:20:25', '2024-03-21 16:20:26');
INSERT INTO `django`.`api_categories` (`category_name`, `category_description`, `category_status`, `created_at`, `updated_at`)
VALUES ('Survival games', 'Survival games start the player off with minimal resources', 0, '2024-03-21 16:20:25', '2024-03-21 16:20:26');
INSERT INTO `django`.`api_categories` (`category_name`, `category_description`, `category_status`, `created_at`, `updated_at`)
VALUES ('MMORPG', 'Massively multiplayer online role-playing games', 0, '2024-03-21 16:20:25', '2024-03-21 16:20:26');
INSERT INTO `django`.`api_categories` (`category_name`, `category_description`, `category_status`, `created_at`, `updated_at`)
VALUES ('Rhythm games', 'Rhythm game or rhythm action is a genre of music-themed action', 0, '2024-03-21 16:20:25', '2024-03-21 16:20:26');


-- Comments
SELECT * FROM api_comment
INSERT INTO `django`.`api_comment` (`comment_author`, `comment_content`, `comment_status`, `created_at`, `updated_at`)
VALUES ('NUTS_NUGS', 'It is the best', 1, '2024-03-21 16:30:40', '2024-03-21 16:30:41');
INSERT INTO `django`.`api_comment` (`comment_author`, `comment_content`, `comment_status`, `created_at`, `updated_at`)
VALUES ('Zatara', 'I prefer board games', 1, '2024-03-21 16:30:40', '2024-03-21 16:30:41');
INSERT INTO `django`.`api_comment` (`comment_author`, `comment_content`, `comment_status`, `created_at`, `updated_at`)
VALUES ('Sid', 'it could be better', 1, '2024-03-21 16:30:40', '2024-03-21 16:30:41');
INSERT INTO `django`.`api_comment` (`comment_author`, `comment_content`, `comment_status`, `created_at`, `updated_at`)
VALUES ('Key', 'It is no that bad', 1, '2024-03-21 16:30:40', '2024-03-21 16:30:41');
INSERT INTO `django`.`api_comment` (`comment_author`, `comment_content`, `comment_status`, `created_at`, `updated_at`)
VALUES ('white', 'It is fun', 1, '2024-03-21 16:30:40', '2024-03-21 16:30:41');



-- User
SELECT * FROM api_user
INSERT INTO `django`.`api_user` (`first_name`, `last_name`, `email`, `psw`, `user_status`, `created_at`, `updated_at`)
VALUES ('NUTS_NUGS', 'one', 'userone@test.com', 'psw1', 1, '2024-03-21 16:44:38', '2024-03-21 16:44:40');
INSERT INTO `django`.`api_user` (`first_name`, `last_name`, `email`, `psw`, `user_status`, `created_at`, `updated_at`)
VALUES ('Zatara', 'two', 'usertwo@test.com', 'psw2', 1, '2024-03-21 16:44:38', '2024-03-21 16:44:40');
INSERT INTO `django`.`api_user` (`first_name`, `last_name`, `email`, `psw`, `user_status`, `created_at`, `updated_at`)
VALUES ('Sid', 'three', 'userthree@test.com', 'psw3', 1, '2024-03-21 16:44:38', '2024-03-21 16:44:40');
INSERT INTO `django`.`api_user` (`first_name`, `last_name`, `email`, `psw`, `user_status`, `created_at`, `updated_at`)
VALUES ('white', 'four', 'userfour@test.com', 'psw4', 1, '2024-03-21 16:44:38', '2024-03-21 16:44:40');
INSERT INTO `django`.`api_user` (`first_name`, `last_name`, `email`, `psw`, `user_status`, `created_at`, `updated_at`)
VALUES ('Key', 'four', 'userfour@test.com', 'psw4', 1, '2024-03-21 16:44:38', '2024-03-21 16:44:40');



-- Post
SELECT * FROM api_post
INSERT INTO `django`.`api_post` (`post_title`, `post_description`, `category_fk_id`, `comments_fk_id`, `user_fk_id`, `created_at`, `updated_at`)
VALUES ('First Post', 'First post description', 1, 3, 3, '2024-03-21 16:48:42', '2024-03-21 16:48:44');
INSERT INTO `django`.`api_post` (`post_title`, `post_description`, `category_fk_id`, `comments_fk_id`, `user_fk_id`, `created_at`, `updated_at`)
VALUES ('Second Post', 'Second post description', 2, 1, 4, '2024-03-21 16:48:42', '2024-03-21 16:48:44');
INSERT INTO `django`.`api_post` (`post_title`, `post_description`, `category_fk_id`, `comments_fk_id`, `user_fk_id`, `created_at`, `updated_at`)
VALUES ('Third Post', 'Third post description', 1, 2, 3, '2024-03-21 16:48:42', '2024-03-21 16:48:44');
INSERT INTO `django`.`api_post` (`post_title`, `post_description`, `category_fk_id`, `comments_fk_id`, `user_fk_id`, `created_at`, `updated_at`)
VALUES ('Fourth Post', 'Fourth post description', 3, 2, 1, '2024-03-21 16:48:42', '2024-03-21 16:48:44');
INSERT INTO `django`.`api_post` (`post_title`, `post_description`, `category_fk_id`, `comments_fk_id`, `user_fk_id`, `created_at`, `updated_at`)
VALUES ('Fifth Post', 'Fifth post description', 1, 1, 1, '2024-03-21 16:48:42', '2024-03-21 16:48:44');