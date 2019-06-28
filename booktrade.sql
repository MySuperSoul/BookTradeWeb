/*
 Navicat Premium Data Transfer

 Source Server         : Rothyu
 Source Server Type    : MySQL
 Source Server Version : 80015
 Source Host           : localhost:3306
 Source Schema         : booktrade

 Target Server Type    : MySQL
 Target Server Version : 80015
 File Encoding         : 65001

 Date: 29/06/2019 00:35:12
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
BEGIN;
INSERT INTO `auth_permission` VALUES (1, 'Can add user', 1, 'add_user');
INSERT INTO `auth_permission` VALUES (2, 'Can change user', 1, 'change_user');
INSERT INTO `auth_permission` VALUES (3, 'Can delete user', 1, 'delete_user');
INSERT INTO `auth_permission` VALUES (4, 'Can view user', 1, 'view_user');
INSERT INTO `auth_permission` VALUES (5, 'Can add log entry', 2, 'add_logentry');
INSERT INTO `auth_permission` VALUES (6, 'Can change log entry', 2, 'change_logentry');
INSERT INTO `auth_permission` VALUES (7, 'Can delete log entry', 2, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (8, 'Can view log entry', 2, 'view_logentry');
INSERT INTO `auth_permission` VALUES (9, 'Can add permission', 3, 'add_permission');
INSERT INTO `auth_permission` VALUES (10, 'Can change permission', 3, 'change_permission');
INSERT INTO `auth_permission` VALUES (11, 'Can delete permission', 3, 'delete_permission');
INSERT INTO `auth_permission` VALUES (12, 'Can view permission', 3, 'view_permission');
INSERT INTO `auth_permission` VALUES (13, 'Can add group', 4, 'add_group');
INSERT INTO `auth_permission` VALUES (14, 'Can change group', 4, 'change_group');
INSERT INTO `auth_permission` VALUES (15, 'Can delete group', 4, 'delete_group');
INSERT INTO `auth_permission` VALUES (16, 'Can view group', 4, 'view_group');
INSERT INTO `auth_permission` VALUES (17, 'Can add content type', 5, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (18, 'Can change content type', 5, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (19, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (20, 'Can view content type', 5, 'view_contenttype');
INSERT INTO `auth_permission` VALUES (21, 'Can add session', 6, 'add_session');
INSERT INTO `auth_permission` VALUES (22, 'Can change session', 6, 'change_session');
INSERT INTO `auth_permission` VALUES (23, 'Can delete session', 6, 'delete_session');
INSERT INTO `auth_permission` VALUES (24, 'Can view session', 6, 'view_session');
INSERT INTO `auth_permission` VALUES (25, 'Can add book', 7, 'add_book');
INSERT INTO `auth_permission` VALUES (26, 'Can change book', 7, 'change_book');
INSERT INTO `auth_permission` VALUES (27, 'Can delete book', 7, 'delete_book');
INSERT INTO `auth_permission` VALUES (28, 'Can view book', 7, 'view_book');
INSERT INTO `auth_permission` VALUES (29, 'Can add comment', 8, 'add_comment');
INSERT INTO `auth_permission` VALUES (30, 'Can change comment', 8, 'change_comment');
INSERT INTO `auth_permission` VALUES (31, 'Can delete comment', 8, 'delete_comment');
INSERT INTO `auth_permission` VALUES (32, 'Can view comment', 8, 'view_comment');
INSERT INTO `auth_permission` VALUES (33, 'Can add shopping car', 9, 'add_shoppingcar');
INSERT INTO `auth_permission` VALUES (34, 'Can change shopping car', 9, 'change_shoppingcar');
INSERT INTO `auth_permission` VALUES (35, 'Can delete shopping car', 9, 'delete_shoppingcar');
INSERT INTO `auth_permission` VALUES (36, 'Can view shopping car', 9, 'view_shoppingcar');
INSERT INTO `auth_permission` VALUES (37, 'Can add book offer', 10, 'add_bookoffer');
INSERT INTO `auth_permission` VALUES (38, 'Can change book offer', 10, 'change_bookoffer');
INSERT INTO `auth_permission` VALUES (39, 'Can delete book offer', 10, 'delete_bookoffer');
INSERT INTO `auth_permission` VALUES (40, 'Can view book offer', 10, 'view_bookoffer');
INSERT INTO `auth_permission` VALUES (41, 'Can add credit account', 11, 'add_creditaccount');
INSERT INTO `auth_permission` VALUES (42, 'Can change credit account', 11, 'change_creditaccount');
INSERT INTO `auth_permission` VALUES (43, 'Can delete credit account', 11, 'delete_creditaccount');
INSERT INTO `auth_permission` VALUES (44, 'Can view credit account', 11, 'view_creditaccount');
INSERT INTO `auth_permission` VALUES (45, 'Can add book need', 12, 'add_bookneed');
INSERT INTO `auth_permission` VALUES (46, 'Can change book need', 12, 'change_bookneed');
INSERT INTO `auth_permission` VALUES (47, 'Can delete book need', 12, 'delete_bookneed');
INSERT INTO `auth_permission` VALUES (48, 'Can view book need', 12, 'view_bookneed');
INSERT INTO `auth_permission` VALUES (49, 'Can add chatting message', 13, 'add_chattingmessage');
INSERT INTO `auth_permission` VALUES (50, 'Can change chatting message', 13, 'change_chattingmessage');
INSERT INTO `auth_permission` VALUES (51, 'Can delete chatting message', 13, 'delete_chattingmessage');
INSERT INTO `auth_permission` VALUES (52, 'Can view chatting message', 13, 'view_chattingmessage');
COMMIT;

-- ----------------------------
-- Table structure for books_book
-- ----------------------------
DROP TABLE IF EXISTS `books_book`;
CREATE TABLE `books_book` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `book_name` varchar(100) NOT NULL,
  `origin_price` int(11) NOT NULL,
  `sell_price` int(11) NOT NULL,
  `category` varchar(100) NOT NULL,
  `book_introduction` longtext NOT NULL,
  `book_image` varchar(100) NOT NULL,
  `ISBN` varchar(100) NOT NULL,
  `book_url` varchar(100) NOT NULL,
  `publisher_name_id` int(11) NOT NULL,
  `store_remain_num` int(11) NOT NULL,
  `trade_way` varchar(100) NOT NULL,
  `publish_time` datetime(6) NOT NULL,
  `book_status` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `books_book_publisher_name_id_c038a438_fk_useraction_user_id` (`publisher_name_id`),
  CONSTRAINT `books_book_publisher_name_id_c038a438_fk_useraction_user_id` FOREIGN KEY (`publisher_name_id`) REFERENCES `useraction_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of books_book
-- ----------------------------
BEGIN;
INSERT INTO `books_book` VALUES (3, 'deep learning', 119, 100, '科技', 'AI圣经 deep learning中文版 2018年图灵奖获奖者作品 业内人称“花书” 人工智能机器学习深度学习领域奠基性经典畅销书 ', 'books/book_3.jpg', '9787115461476', 'http://product.dangdang.com/25111382.html#ddclick_reco_reco_buytogether', 1, 18, 'online', '2019-06-11 10:20:33.618302', 0);
INSERT INTO `books_book` VALUES (4, 'TensorFlow技术解析与实战', 39, 20, '科技', '机器学习深度学习领域参考书 包揽TensorFlow1.1的新特性 人脸识别 语音识别 图像和语音相结合等热点一应俱全 李航 余凯等人工智能领域专家倾力推荐 ', 'books/book_4.jpg', '9787115456137', 'http://product.dangdang.com/25073507.html#ddclick_reco_reco_relate', 1, 10, 'online', '2019-06-11 10:20:33.618302', 0);
INSERT INTO `books_book` VALUES (5, '机器学习', 66, 50, '科技', '击败AlphaGo的武林秘籍，赢得人机大战的必由之路：人工智能大牛周志华教授巨著，全面揭开机器学习的奥秘 ', 'books/book_5.jpg', '9787302423287', 'http://product.dangdang.com/23898620.html', 1, 7, 'online', '2019-06-11 10:20:33.618302', 0);
INSERT INTO `books_book` VALUES (6, 'Keras深度学习实战', 30, 15, '科技', '作为一款轻量级、模块化的开源深度学习框架，Keras以容易上手、利于快速原型实现、能够与TensorFlow和Theano等后端计算平台很好兼容等优点，深受众多开发人员和研究人员的喜爱。 本书结合大量实例，简明扼要地介绍了目前热门的神经网络技术和深度学习技术。从经典的多层感知机到用于图像处理的深度卷积网络，从处理序列化数据的循环网络到伪造仿真数据的生成对抗网络，从词嵌入到AI游戏应用中的强化学习，本书引ling读者一层一层揭开深度学习的面纱，并在逐渐清晰的理论框架下，提供多个Python编码实例，方便读者动手实践。 通过阅读本书，读者不仅能学会使用Keras快捷构建各个类型的深度网络，还可以按需自定义网络层和后端功能，从而提升自己的AI编程能力，在成为深度学习专家的路上更进一步。', 'books/book_6.jpg', '9787115482228', 'http://product.dangdang.com/25295969.html#ddclick_reco_reco_relate', 1, 9, 'offline', '2019-06-11 10:20:33.618302', 0);
INSERT INTO `books_book` VALUES (7, '人生海海', 55, 20, '人文社科', '人生海海，何必在意一时沉浮！《风声》作家、茅盾文学奖得主麦家2019强力之作，挑战常人不敢落笔之处，解密人性的荒唐与高尚。', 'books/book_7.jpg', '9787530219218', 'http://product.dangdang.com/26921715.html', 3, 19, 'online', '2019-06-11 11:39:09.386512', 0);
INSERT INTO `books_book` VALUES (9, '菊与刀', 10, 5, '人文社科', '解读日本矛盾国民性格的经典读物，学术著作因流畅精彩的译文变得相当好看。它直接影响了战后美日关系格局，是社会研究直接运用于政治实际操作的杰出范例！就从这里开始了解日本！ ', 'books/book_9.jpg', '9787533945510', 'http://product.dangdang.com/23981714.html', 3, 0, '', '2019-06-17 11:41:47.795033', 1);
INSERT INTO `books_book` VALUES (11, '人间失格', 15, 10, '教育', '超燃！“丧文化”流行，《人间失格》成了现象级畅销书，创当当3天销售50000+册的奇迹！收录作者绝笔之作《Good bye》。一个“丧失为人资格”少年的心灵独白，一个对村上春树影响至深的绝望凄美故事。', 'books/book_11.jpg', '9787506380263', 'http://product.dangdang.com/23761145.html', 4, 10, 'online', '2019-06-21 02:18:23.987233', 0);
INSERT INTO `books_book` VALUES (12, '有一个地方叫夏', 85, 50, '励志', '忘记，是因为曾经记得。是否好好告别过，与那些你曾创造的，爱过的，又遗忘的一切？意大利天才画家力作，虚构遗忘物之城——夏城，探讨“告别”的哲学。', 'books/book_12.jpg', '9787559628091', 'http://product.dangdang.com/27870507.html', 4, 10, 'offline', '2019-06-21 02:20:32.615108', 0);
INSERT INTO `books_book` VALUES (13, '和孩子聊艺术', 61, 30, '童书', '一本深深影响孩子成长的艺术启蒙书，一本让孩子了解世界艺术史的通识读本。让每个孩子喜欢艺术，懂得欣赏艺术，了解艺术的历史进程！（蒲公英童书馆出品）', 'books/book_13.jpg', '9787221144058', 'http://product.dangdang.com/26921711.html', 3, 4, 'online', '2019-06-21 02:33:56.856782', 0);
INSERT INTO `books_book` VALUES (14, '孩子受益一生的思维力', 34, 20, '生活', '美国幼儿园和小学都在使用的学习工具。一看就懂、一学就能上手的八大思维导图，阅读、写作、演讲、课堂学习……处处都受用的思维方法，让摸不着看不见的思维过程直观呈现，帮助孩子学习力...', 'books/book_14.jpg', '9787554613122', 'http://product.dangdang.com/26445780.html', 3, 10, 'online', '2019-06-21 02:46:42.046019', 0);
INSERT INTO `books_book` VALUES (15, '埃及四千年', 93, 50, '人文社科', '上市7天即告售罄！当当4.23书香节读者*爱的人文社科类榜首图书！BBC古埃及历史纪录片原著主宰世界历史进程的宏大史诗《出版人周刊》《科克斯书评》2016年度图书《华盛顿邮报》等30家知名媒体联名推荐', 'books/book_15.jpg', '9787533954482', 'http://product.dangdang.com/26917419.html', 5, 23, 'offline', '2019-06-21 02:50:32.239223', 0);
INSERT INTO `books_book` VALUES (16, '福尔摩斯探案全集', 74, 40, '教育', '《福尔摩斯探案全集》被称为推理小说中的“圣经”，一百多年来被译成57种文字，畅销世界各地。福尔摩斯更是成了名侦探的代名词，他与华生的搭档组合，以及“神探”的典型等，都对后世的侦探小说有着极其深远的影响。英国著名小说家毛姆曾说：“和柯南道尔所写的《福尔摩斯探案全集》相比，没有任何侦探小说曾享有那么大的声誉。”', 'books/book_16.jpg', '9787530955574', 'http://product.dangdang.com/20531088.html', 5, 10, 'offline', '2019-06-27 06:50:14.941532', 0);
INSERT INTO `books_book` VALUES (18, '少年读史记', 59, 30, '童书', '精巧32开本，当当独家定制版。荣获第六届中华优秀出版物奖 ；史学、文学、哲学、国学一次到位，台湾著名儿童文学作家张嘉骅倾力打造更适合孩子阅读的《史记》！', 'books/book_18.jpg', '23778791', 'http://product.dangdang.com/23778791.html', 1, 10, 'online', '2019-06-28 02:51:28.126401', 0);
INSERT INTO `books_book` VALUES (19, '墨菲定律', 20, 10, '人文社科', '（受益一生的墨菲定律，一本好玩又实用的日常行为心理指南；突破思维界限，认识真正的自我；揭示那些无处不在左右你生活的心理学秘密，原来，那些让人发笑却又令人深思的行为的背后，都藏着好玩又古怪的心理效应。）', 'books/book_19.jpg', '9787554609491', 'http://product.dangdang.com/25142121.html', 1, 0, '', '2019-06-28 02:57:36.595779', 1);
COMMIT;

-- ----------------------------
-- Table structure for books_bookneed
-- ----------------------------
DROP TABLE IF EXISTS `books_bookneed`;
CREATE TABLE `books_bookneed` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `message` longtext NOT NULL,
  `book_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `books_bookneed_book_id_bd87ea9d_fk_books_book_id` (`book_id`),
  CONSTRAINT `books_bookneed_book_id_bd87ea9d_fk_books_book_id` FOREIGN KEY (`book_id`) REFERENCES `books_book` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of books_bookneed
-- ----------------------------
BEGIN;
INSERT INTO `books_bookneed` VALUES (2, '八成新即可 有可联系我 17367078037', 9);
INSERT INTO `books_bookneed` VALUES (3, '想看这本书学心理学，联系我：17367078037', 19);
COMMIT;

-- ----------------------------
-- Table structure for books_bookoffer
-- ----------------------------
DROP TABLE IF EXISTS `books_bookoffer`;
CREATE TABLE `books_bookoffer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sell_option` longtext NOT NULL,
  `post_address` longtext NOT NULL,
  `post_code` longtext NOT NULL,
  `status` longtext NOT NULL,
  `complete_time` datetime(6) NOT NULL,
  `book_id` int(11) NOT NULL,
  `buy_side_id` int(11) NOT NULL,
  `sell_side_id` int(11) NOT NULL,
  `complete_book_num` int(11) NOT NULL,
  `complete_price` int(11) NOT NULL,
  `contact_phone` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `books_bookoffer_book_id_20740ab3_fk_books_book_id` (`book_id`),
  KEY `books_bookoffer_buy_side_id_75b10c8d_fk_useraction_user_id` (`buy_side_id`),
  KEY `books_bookoffer_sell_side_id_21f229ba_fk_useraction_user_id` (`sell_side_id`),
  CONSTRAINT `books_bookoffer_book_id_20740ab3_fk_books_book_id` FOREIGN KEY (`book_id`) REFERENCES `books_book` (`id`),
  CONSTRAINT `books_bookoffer_buy_side_id_75b10c8d_fk_useraction_user_id` FOREIGN KEY (`buy_side_id`) REFERENCES `useraction_user` (`id`),
  CONSTRAINT `books_bookoffer_sell_side_id_21f229ba_fk_useraction_user_id` FOREIGN KEY (`sell_side_id`) REFERENCES `useraction_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of books_bookoffer
-- ----------------------------
BEGIN;
INSERT INTO `books_bookoffer` VALUES (5, 'offline', '浙江大学玉泉校区', '', 'complete', '2019-06-13 13:13:16.486544', 6, 3, 1, 1, 15, '17367078037');
INSERT INTO `books_bookoffer` VALUES (6, 'offline', '浙江大学玉泉校区', '', 'complete', '2019-06-14 06:36:34.543384', 6, 3, 1, 1, 15, '17367078037');
INSERT INTO `books_bookoffer` VALUES (7, 'online', '杭州市', '', 'complete', '2019-06-14 06:44:37.182309', 5, 3, 1, 2, 100, '15932955084');
INSERT INTO `books_bookoffer` VALUES (8, 'online', 'campus yuquan', '', 'complete', '2019-06-15 04:26:52.578971', 3, 3, 1, 2, 200, '8818007');
INSERT INTO `books_bookoffer` VALUES (9, 'offline', '之江校区', '', 'complete', '2019-06-17 14:21:45.360028', 6, 1, 3, 1, 15, '8818007');
INSERT INTO `books_bookoffer` VALUES (10, 'online', 'yuquan', '', 'complete', '2019-06-21 03:38:40.048741', 7, 1, 3, 1, 20, '8818007');
INSERT INTO `books_bookoffer` VALUES (11, 'online', '浙江大学玉泉校区5舍', '', 'complete', '2019-06-28 03:09:59.593275', 13, 1, 3, 2, 60, '17367078037');
COMMIT;

-- ----------------------------
-- Table structure for books_comment
-- ----------------------------
DROP TABLE IF EXISTS `books_comment`;
CREATE TABLE `books_comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `time` datetime(6) NOT NULL,
  `content` longtext NOT NULL,
  `book_id` int(11) NOT NULL,
  `commenter_id` int(11) NOT NULL,
  `score` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `books_comment_book_id_ac8af439_fk_books_book_id` (`book_id`),
  KEY `books_comment_commenter_id_91139e93_fk_useraction_user_id` (`commenter_id`),
  CONSTRAINT `books_comment_book_id_ac8af439_fk_books_book_id` FOREIGN KEY (`book_id`) REFERENCES `books_book` (`id`),
  CONSTRAINT `books_comment_commenter_id_91139e93_fk_useraction_user_id` FOREIGN KEY (`commenter_id`) REFERENCES `useraction_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of books_comment
-- ----------------------------
BEGIN;
INSERT INTO `books_comment` VALUES (1, '2019-06-08 08:04:31.858631', 'Tensorflow技术讲解的很详细，不错', 4, 1, 5);
INSERT INTO `books_comment` VALUES (2, '2019-06-08 08:56:05.261510', '不过纸张好像有点尴尬。。。', 4, 1, 4);
INSERT INTO `books_comment` VALUES (3, '2019-06-08 09:02:20.603651', '你这书也卖的太贵了叭兄弟', 4, 2, 3);
INSERT INTO `books_comment` VALUES (4, '2019-06-12 04:19:12.705222', '很好的一本书了。', 6, 1, 4);
INSERT INTO `books_comment` VALUES (5, '2019-06-17 12:37:30.946068', '有书的带带我！', 9, 1, 5);
INSERT INTO `books_comment` VALUES (6, '2019-06-27 06:33:29.566204', '还行，想买', 12, 1, 4);
INSERT INTO `books_comment` VALUES (7, '2019-06-27 06:35:54.288693', '真的挺好的一本书', 12, 1, 5);
INSERT INTO `books_comment` VALUES (8, '2019-06-27 17:36:15.040758', '这本书真的非常不错的啊！！', 3, 1, 5);
COMMIT;

-- ----------------------------
-- Table structure for books_creditaccount
-- ----------------------------
DROP TABLE IF EXISTS `books_creditaccount`;
CREATE TABLE `books_creditaccount` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `account_money` int(11) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `account_owner_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `books_creditaccount_account_owner_id_7316ed2a_fk_useractio` (`account_owner_id`),
  CONSTRAINT `books_creditaccount_account_owner_id_7316ed2a_fk_useractio` FOREIGN KEY (`account_owner_id`) REFERENCES `useraction_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of books_creditaccount
-- ----------------------------
BEGIN;
INSERT INTO `books_creditaccount` VALUES (1, 140, '2019-06-15 13:30:05.000000', 1);
INSERT INTO `books_creditaccount` VALUES (2, 100, '2019-06-15 13:30:49.000000', 2);
INSERT INTO `books_creditaccount` VALUES (3, 105, '2019-06-15 13:31:03.000000', 3);
INSERT INTO `books_creditaccount` VALUES (4, 100, '2019-06-15 13:31:20.000000', 4);
INSERT INTO `books_creditaccount` VALUES (5, 140, '2019-06-16 15:56:28.744587', 5);
COMMIT;

-- ----------------------------
-- Table structure for books_shoppingcar
-- ----------------------------
DROP TABLE IF EXISTS `books_shoppingcar`;
CREATE TABLE `books_shoppingcar` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `added_number` int(11) NOT NULL,
  `book_id` int(11) NOT NULL,
  `book_owner_id` int(11) NOT NULL,
  `address` longtext NOT NULL,
  `contact_phone` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `books_shoppingcar_book_id_6b6f8506_fk_books_book_id` (`book_id`),
  KEY `books_shoppingcar_book_owner_id_b28066e9_fk_useraction_user_id` (`book_owner_id`),
  CONSTRAINT `books_shoppingcar_book_id_6b6f8506_fk_books_book_id` FOREIGN KEY (`book_id`) REFERENCES `books_book` (`id`),
  CONSTRAINT `books_shoppingcar_book_owner_id_b28066e9_fk_useraction_user_id` FOREIGN KEY (`book_owner_id`) REFERENCES `useraction_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of books_shoppingcar
-- ----------------------------
BEGIN;
INSERT INTO `books_shoppingcar` VALUES (18, 3, 12, 3, '图书馆1楼', '15932955084');
INSERT INTO `books_shoppingcar` VALUES (19, 2, 11, 1, '浙江大学玉泉校区5舍', '17367078037');
COMMIT;

-- ----------------------------
-- Table structure for chatting_chattingmessage
-- ----------------------------
DROP TABLE IF EXISTS `chatting_chattingmessage`;
CREATE TABLE `chatting_chattingmessage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `message` longtext NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `recv_side_id` int(11) NOT NULL,
  `send_side_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `chatting_chattingmes_recv_side_id_27b7fcf4_fk_useractio` (`recv_side_id`),
  KEY `chatting_chattingmes_send_side_id_d4dc148f_fk_useractio` (`send_side_id`),
  CONSTRAINT `chatting_chattingmes_recv_side_id_27b7fcf4_fk_useractio` FOREIGN KEY (`recv_side_id`) REFERENCES `useraction_user` (`id`),
  CONSTRAINT `chatting_chattingmes_send_side_id_d4dc148f_fk_useractio` FOREIGN KEY (`send_side_id`) REFERENCES `useraction_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of chatting_chattingmessage
-- ----------------------------
BEGIN;
INSERT INTO `chatting_chattingmessage` VALUES (1, '我想买这本书', '2019-06-19 08:30:00.926814', 1, 3);
INSERT INTO `chatting_chattingmessage` VALUES (2, '好啊，30块就可以了～', '2019-06-19 08:47:56.830400', 3, 1);
INSERT INTO `chatting_chattingmessage` VALUES (3, '那行，明天见', '2019-06-19 08:48:06.833666', 1, 3);
INSERT INTO `chatting_chattingmessage` VALUES (4, '拜拜', '2019-06-19 08:48:13.812333', 3, 1);
INSERT INTO `chatting_chattingmessage` VALUES (5, '我想买2本', '2019-06-19 08:49:50.639860', 1, 3);
INSERT INTO `chatting_chattingmessage` VALUES (6, '都行的～', '2019-06-19 08:50:08.568367', 3, 1);
INSERT INTO `chatting_chattingmessage` VALUES (7, '吼的，我要两本', '2019-06-19 11:05:45.202662', 1, 3);
INSERT INTO `chatting_chattingmessage` VALUES (8, '再来两本', '2019-06-19 11:14:43.351136', 1, 3);
INSERT INTO `chatting_chattingmessage` VALUES (9, 'emmmm，太真实了吧', '2019-06-19 12:04:38.935227', 1, 3);
INSERT INTO `chatting_chattingmessage` VALUES (10, '真的坑啊', '2019-06-19 13:00:21.212641', 1, 3);
INSERT INTO `chatting_chattingmessage` VALUES (11, '对啊', '2019-06-19 13:00:36.465953', 3, 1);
INSERT INTO `chatting_chattingmessage` VALUES (12, '发条信息', '2019-06-19 15:39:29.142600', 1, 3);
INSERT INTO `chatting_chattingmessage` VALUES (13, '拜拜，下线了', '2019-06-19 15:40:01.385300', 3, 1);
INSERT INTO `chatting_chattingmessage` VALUES (14, '早上好', '2019-06-20 04:19:57.235435', 3, 1);
INSERT INTO `chatting_chattingmessage` VALUES (15, '你好', '2019-06-20 04:20:12.321973', 1, 3);
INSERT INTO `chatting_chattingmessage` VALUES (16, '我要买书', '2019-06-21 02:35:49.990992', 4, 3);
INSERT INTO `chatting_chattingmessage` VALUES (17, 'yifei中午好，马上要提交BS作业了，我想多买两本书可以嘛', '2019-06-28 03:44:45.177690', 3, 1);
INSERT INTO `chatting_chattingmessage` VALUES (18, '吼啊吼啊，找我买就对了，稳的', '2019-06-28 03:50:37.935239', 1, 3);
COMMIT;

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_useraction_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_useraction_user_id` FOREIGN KEY (`user_id`) REFERENCES `useraction_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
BEGIN;
INSERT INTO `django_content_type` VALUES (2, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (4, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (7, 'books', 'book');
INSERT INTO `django_content_type` VALUES (12, 'books', 'bookneed');
INSERT INTO `django_content_type` VALUES (10, 'books', 'bookoffer');
INSERT INTO `django_content_type` VALUES (8, 'books', 'comment');
INSERT INTO `django_content_type` VALUES (11, 'books', 'creditaccount');
INSERT INTO `django_content_type` VALUES (9, 'books', 'shoppingcar');
INSERT INTO `django_content_type` VALUES (13, 'chatting', 'chattingmessage');
INSERT INTO `django_content_type` VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (6, 'sessions', 'session');
INSERT INTO `django_content_type` VALUES (1, 'useraction', 'user');
COMMIT;

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
BEGIN;
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2019-05-22 05:24:56.915338');
INSERT INTO `django_migrations` VALUES (2, 'contenttypes', '0002_remove_content_type_name', '2019-05-22 05:24:57.524378');
INSERT INTO `django_migrations` VALUES (3, 'auth', '0001_initial', '2019-05-22 05:24:58.619365');
INSERT INTO `django_migrations` VALUES (4, 'auth', '0002_alter_permission_name_max_length', '2019-05-22 05:24:59.529233');
INSERT INTO `django_migrations` VALUES (5, 'auth', '0003_alter_user_email_max_length', '2019-05-22 05:24:59.675329');
INSERT INTO `django_migrations` VALUES (6, 'auth', '0004_alter_user_username_opts', '2019-05-22 05:24:59.817482');
INSERT INTO `django_migrations` VALUES (7, 'auth', '0005_alter_user_last_login_null', '2019-05-22 05:24:59.956697');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0006_require_contenttypes_0002', '2019-05-22 05:25:00.089869');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0007_alter_validators_add_error_messages', '2019-05-22 05:25:00.231008');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0008_alter_user_username_max_length', '2019-05-22 05:25:00.374841');
INSERT INTO `django_migrations` VALUES (11, 'auth', '0009_alter_user_last_name_max_length', '2019-05-22 05:25:00.516591');
INSERT INTO `django_migrations` VALUES (12, 'auth', '0010_alter_group_name_max_length', '2019-05-22 05:25:00.791308');
INSERT INTO `django_migrations` VALUES (13, 'auth', '0011_update_proxy_permissions', '2019-05-22 05:25:01.129775');
INSERT INTO `django_migrations` VALUES (14, 'useraction', '0001_initial', '2019-05-22 05:25:02.927383');
INSERT INTO `django_migrations` VALUES (15, 'admin', '0001_initial', '2019-05-22 05:25:05.106704');
INSERT INTO `django_migrations` VALUES (16, 'admin', '0002_logentry_remove_auto_add', '2019-05-22 05:25:05.545727');
INSERT INTO `django_migrations` VALUES (17, 'admin', '0003_logentry_add_action_flag_choices', '2019-05-22 05:25:05.689474');
INSERT INTO `django_migrations` VALUES (18, 'sessions', '0001_initial', '2019-05-22 05:25:06.122274');
INSERT INTO `django_migrations` VALUES (19, 'useraction', '0002_user_header_image', '2019-05-26 11:07:18.952997');
INSERT INTO `django_migrations` VALUES (20, 'books', '0001_initial', '2019-05-27 01:29:36.568125');
INSERT INTO `django_migrations` VALUES (21, 'useraction', '0003_auto_20190527_0129', '2019-05-27 01:29:36.822642');
INSERT INTO `django_migrations` VALUES (22, 'books', '0002_auto_20190527_1054', '2019-05-27 10:54:58.053224');
INSERT INTO `django_migrations` VALUES (23, 'books', '0003_auto_20190608_1526', '2019-06-08 07:26:16.257460');
INSERT INTO `django_migrations` VALUES (24, 'books', '0004_comment_score', '2019-06-08 07:51:23.245429');
INSERT INTO `django_migrations` VALUES (25, 'books', '0005_shoppingcar', '2019-06-09 16:30:18.357804');
INSERT INTO `django_migrations` VALUES (26, 'books', '0006_book_publish_time', '2019-06-11 10:20:33.691828');
INSERT INTO `django_migrations` VALUES (27, 'books', '0007_bookoffer', '2019-06-13 03:00:36.204124');
INSERT INTO `django_migrations` VALUES (28, 'books', '0008_auto_20190613_2046', '2019-06-13 12:46:10.591693');
INSERT INTO `django_migrations` VALUES (29, 'books', '0009_auto_20190614_1429', '2019-06-14 06:29:46.723517');
INSERT INTO `django_migrations` VALUES (30, 'books', '0010_creditaccount', '2019-06-15 05:28:40.948523');
INSERT INTO `django_migrations` VALUES (31, 'books', '0011_book_book_status', '2019-06-16 16:38:46.143027');
INSERT INTO `django_migrations` VALUES (32, 'books', '0012_auto_20190617_1331', '2019-06-17 05:32:22.331556');
INSERT INTO `django_migrations` VALUES (33, 'books', '0013_bookneed', '2019-06-17 08:17:30.507863');
INSERT INTO `django_migrations` VALUES (34, 'chatting', '0001_initial', '2019-06-18 06:46:00.743634');
INSERT INTO `django_migrations` VALUES (35, 'useraction', '0004_user_channel_name', '2019-06-18 06:46:00.960292');
COMMIT;

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for useraction_user
-- ----------------------------
DROP TABLE IF EXISTS `useraction_user`;
CREATE TABLE `useraction_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `email` varchar(254) NOT NULL,
  `telephone` varchar(20) NOT NULL,
  `introduction` longtext NOT NULL,
  `address` longtext NOT NULL,
  `header_image` varchar(100) NOT NULL,
  `channel_name` longtext NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of useraction_user
-- ----------------------------
BEGIN;
INSERT INTO `useraction_user` VALUES (1, 'pbkdf2_sha256$150000$xx1vRvMBAS9d$Bc41xkZEJtzlsqnw52Ia4+z5+4Lcou4JFgkvsXjhKHw=', '2019-06-28 15:36:25.107721', 0, 'huangyifei', '', '', 0, 1, '2019-05-22 05:26:06.709343', '1144358492@qq.com', '17367078037', 'zju major in SE', 'campus yuquan', 'headers/header_huangyifei.jpg', '');
INSERT INTO `useraction_user` VALUES (2, 'pbkdf2_sha256$150000$DYh7N6gaHzef$r88HoRHa6z7joyZr2SlO8aREK/LD2vCSrj6+qMgurZk=', '2019-06-09 15:06:57.388478', 0, '城源', '', '', 0, 1, '2019-05-22 05:27:04.910208', '114435@fabu.ai', '', '', '', 'headers/default.jpg', '');
INSERT INTO `useraction_user` VALUES (3, 'pbkdf2_sha256$150000$HdqibUueIMAS$4St/8wiCfRY9fDvuCWhe/6bQtj2Q4glTW9/k+ioesdY=', '2019-06-28 13:49:34.028763', 0, 'yifei', '', '', 0, 1, '2019-06-09 16:58:41.189589', '1144358492@163.com', '13807947768', '软件工程学生', '浙江大学玉泉校区', '/headers/default.jpg', '');
INSERT INTO `useraction_user` VALUES (4, 'pbkdf2_sha256$150000$TybtAYtWxv5q$Trdzhnzt1Fx4a8AvOpaubwbcozpIoSsuoNa+G0NhEV8=', '2019-06-21 02:17:18.475427', 0, 'rothyu', '', '', 0, 1, '2019-06-14 16:08:24.396754', 'yifei@gmail.com', '17367078037', 'rothyu卖书了～', '浙江大学玉泉校区5舍226', '/headers/default.jpg', '');
INSERT INTO `useraction_user` VALUES (5, 'pbkdf2_sha256$150000$DMkc0Hp2v9ye$vfxStoZSuMrCE/UDfLzqigiDY1H86XztOAScWpVhcTI=', '2019-06-27 06:47:24.038752', 0, 'zty', '', '', 0, 1, '2019-06-16 15:56:28.565218', '12345678@163.com', '15932955084', 'zty', '浙江省杭州市西溪谷国际商务中心', '/headers/default.jpg', '');
COMMIT;

-- ----------------------------
-- Table structure for useraction_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `useraction_user_groups`;
CREATE TABLE `useraction_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `useraction_user_groups_user_id_group_id_8c4b446f_uniq` (`user_id`,`group_id`),
  KEY `useraction_user_groups_group_id_e6fab733_fk_auth_group_id` (`group_id`),
  CONSTRAINT `useraction_user_groups_group_id_e6fab733_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `useraction_user_groups_user_id_02d79553_fk_useraction_user_id` FOREIGN KEY (`user_id`) REFERENCES `useraction_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for useraction_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `useraction_user_user_permissions`;
CREATE TABLE `useraction_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `useraction_user_user_per_user_id_permission_id_5bb6f665_uniq` (`user_id`,`permission_id`),
  KEY `useraction_user_user_permission_id_cd298454_fk_auth_perm` (`permission_id`),
  CONSTRAINT `useraction_user_user_permission_id_cd298454_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `useraction_user_user_user_id_c9f1563c_fk_useractio` FOREIGN KEY (`user_id`) REFERENCES `useraction_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
