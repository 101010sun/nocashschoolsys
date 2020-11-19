<?php
// MongoDB 伺服器設定
$dbhost = 'localhost';
$dbname = 'nocashschoolsys';
// 連線到 MongoDB 伺服器
$mongoClient = new MongoClient('mongodb://' . $dbhost);
$db = $mongoClient->$dbname;

// 取得 demo 這個 collection
$cactive = $db->active;

// 查詢資料
$result = $cactive->find();
