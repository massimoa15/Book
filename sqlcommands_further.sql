/* These are commands used for updating tables.
 */
 
/*Inserting new users*/
INSERT INTO Users
VALUES ( 'UserID', 'UPassword', 'UBooks', 'UOtherInfo'); /*strings here are just place holder, replace them by real generated strings*/

/*Inserting new books*/
INSERT INTO Books
VALUES ( 'BNumber', 'BTitle', 'BAuthor', 'BISBN', 'BCourse', 'BPic');

/*Inserting new postings*/
INSERT INTO Postings
VALUES ( 'UserID', 'UBooks', 'PostDates');


/* getting course titles through course ID(CourseIDtheUserSelected)
 variable names are just made easier to understand, they can be changed to other names*/
SELECT *
FROM Courses
WHERE CourseID = 'CourseIDthatNeeded'; /*strings can be changed into variables*/


/* deleting users if needed */
DELETE FROM Users
WHERE UserID = 'UserNeedstobeDeleted';


/* getting passwords from a specific user */
SELECT UPassword
FROM Users
WHERE UserID = 'UserNeedstobeChecked';



/* look up all uesers */
SELECT * /*can be changed to any other attributes for specific needs*/
FROM Users;


/* changing/updating information for specific needs */
UPDATE Users
SET UBooks = 'NewBooks' /*a string of BNumber/BISBN in reality*/
WHERE UserID = 'TheUserthatUpdating';
