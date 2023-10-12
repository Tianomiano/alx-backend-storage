-- a trigger that resets the "valid_email"
-- attribute only when the email has been changed
DELIMITER $$ ;
CREATE TRIGGER UpdateValidEmail  BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
        IF NEW.email != OLD.email THEN
                SET NEW.valid_email = 0;
        END if;
END;$$
delimiter;
