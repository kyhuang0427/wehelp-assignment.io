# WeHelp Assigment Week5 - README

將SQL CRUD、SQL Aggregate Functions和SQL JOIN所練習的指令以及指令執⾏畫⾯的截圖呈現出來。

## 目錄

1. SQL CRUD
2. SQL Aggregate Functions
3. SQL JOIN

---

## 1. SQL CRUD

### - 使⽤ INSERT 指令新增⼀筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。接著繼續新增⾄少 4 筆隨意的資料。
SQL Command:
```sql
INSERT INTO member (name, username, password, follower_count)
VALUES ('Test', 'test', 'test', 5);

INSERT INTO member (name, username, password, follower_count)
VALUES ('AAA', 'aaa', 'aaa', 10);

INSERT INTO member (name, username, password, follower_count)
VALUES ('BBB', 'bbb', 'bbb', 15);

INSERT INTO member (name, username, password, follower_count)
VALUES ('CCC', 'ccc', 'ccc', 20);

INSERT INTO member (name, username, password, follower_count)
VALUES ('DDD', 'ddd', 'ddd', 30);
```
指令執⾏畫⾯的截圖:

![SQL CRUD](https://github.com/kyhuang0427/wehelp-assignment.io/blob/1a26cddcc5922078188ae76a9b924f89e4479911/week5/png/3-1.png)

### - 使⽤ SELECT 指令取得所有在 member 資料表中的會員資料。
SQL Command:
```sql
SELECT * FROM member;
```
指令執⾏畫⾯的截圖:

![SQL CRUD](https://github.com/kyhuang0427/wehelp-assignment.io/blob/1a26cddcc5922078188ae76a9b924f89e4479911/week5/png/3-2.png)

### - 使⽤ SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。
SQL Command:
```sql
SELECT * FROM member ORDER BY time DESC;
```
指令執⾏畫⾯的截圖:

![SQL CRUD](https://github.com/kyhuang0427/wehelp-assignment.io/blob/1a26cddcc5922078188ae76a9b924f89e4479911/week5/png/3-3.png)

### - 使⽤ SELECT 指令取得 member 資料表中第 2 到第 4 筆共三筆資料，並按照 time 欄位，由近到遠排序。 ( 並非編號 2、3、4 的資料，⽽是排序後的第 2 ~ 4 筆資料 )
SQL Command:
```sql
SELECT * FROM member ORDER BY time DESC LIMIT 3 OFFSET 1;
```
指令執⾏畫⾯的截圖:

![SQL CRUD](https://github.com/kyhuang0427/wehelp-assignment.io/blob/1a26cddcc5922078188ae76a9b924f89e4479911/week5/png/3-4.png)

### - 使⽤ SELECT 指令取得欄位 username 是 test 的會員資料。
SQL Command:
```sql
SELECT * FROM member WHERE username = 'test';
```
指令執⾏畫⾯的截圖:

![SQL CRUD](https://github.com/kyhuang0427/wehelp-assignment.io/blob/1a26cddcc5922078188ae76a9b924f89e4479911/week5/png/3-5.png)

### - 使⽤ SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。
SQL Command:
```sql
SELECT * FROM member WHERE username = 'test' AND password = 'test';
```
指令執⾏畫⾯的截圖:

![SQL CRUD](https://github.com/kyhuang0427/wehelp-assignment.io/blob/1a26cddcc5922078188ae76a9b924f89e4479911/week5/png/3-6.png)

### - 使⽤ UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。
SQL Command:
```sql
UPDATE member SET name = 'test2' WHERE username = 'test';
```
指令執⾏畫⾯的截圖:

![SQL CRUD](https://github.com/kyhuang0427/wehelp-assignment.io/blob/1a26cddcc5922078188ae76a9b924f89e4479911/week5/png/3-7.png)

## 2. SQL Aggregate Functions
### - 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。
SQL Command:
```sql
SELECT COUNT(*) FROM member;
```
指令執⾏畫⾯的截圖:

![SQL Aggregate Functions](https://github.com/kyhuang0427/wehelp-assignment.io/blob/1a26cddcc5922078188ae76a9b924f89e4479911/week5/png/4-1.png)

### - 取得 member 資料表中，所有會員 follower_count 欄位的總和。
SQL Command:
```sql
SELECT SUM(follower_count) FROM member;
```
指令執⾏畫⾯的截圖:

![SQL Aggregate Functions](https://github.com/kyhuang0427/wehelp-assignment.io/blob/1a26cddcc5922078188ae76a9b924f89e4479911/week5/png/4-2.png)

### - 取得 member 資料表中，所有會員 follower_count 欄位的平均數。
SQL Command:
```sql
SELECT AVG(follower_count) FROM member;
```
![SQL Aggregate Functions](https://github.com/kyhuang0427/wehelp-assignment.io/blob/1a26cddcc5922078188ae76a9b924f89e4479911/week5/png/4-3.png)

## 3. SQL JOIN
### - 使⽤ SELECT 搭配 JOIN 語法，取得所有留⾔，結果須包含留⾔者的姓名。
SQL Command:
```sql
SELECT message.id, member.name AS sender_name, message.content, message.like_count, message.time
FROM message
JOIN member ON message.member_id = member.id;
```
指令執⾏畫⾯的截圖:

![SQL JOIN](https://github.com/kyhuang0427/wehelp-assignment.io/blob/1a26cddcc5922078188ae76a9b924f89e4479911/week5/png/5-1.png)

### - 使⽤ SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留⾔，資料中須包含留⾔者的姓名。
SQL Command:
```sql
SELECT message.id, member.name AS sender_name, message.content, message.like_count, message.time
FROM message
JOIN member ON message.member_id = member.id
WHERE member.username = 'test';
```
指令執⾏畫⾯的截圖:

![SQL JOIN](https://github.com/kyhuang0427/wehelp-assignment.io/blob/1a26cddcc5922078188ae76a9b924f89e4479911/week5/png/5-2.png)

### - 使⽤ SELECT、SQL Aggregate Functions 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留⾔平均按讚數。
SQL Command:
```sql
SELECT member.username, AVG(message.like_count) AS average_likes
FROM member
JOIN message ON member.id = message.member_id
WHERE member.username = 'test'
GROUP BY member.username;
```
指令執⾏畫⾯的截圖:

![SQL JOIN](https://github.com/kyhuang0427/wehelp-assignment.io/blob/1a26cddcc5922078188ae76a9b924f89e4479911/week5/png/5-3.png)






