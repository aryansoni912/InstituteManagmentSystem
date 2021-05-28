-- phpMyAdmin SQL Dump
-- version 4.1.14
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: May 28, 2021 at 10:37 AM
-- Server version: 5.6.17
-- PHP Version: 5.5.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `institute`
--

-- --------------------------------------------------------

--
-- Stand-in structure for view `attendace_detail`
--
CREATE TABLE IF NOT EXISTS `attendace_detail` (
`No` int(5)
,`Email_id` varchar(100)
,`Contact` text
,`Name` varchar(50)
,`Password` varchar(30)
,`Mname` varchar(50)
,`lname` varchar(30)
,`gender` varchar(11)
,`bdate` date
,`course` varchar(50)
,`address` varchar(300)
,`img` varchar(250)
,`Day` varchar(10)
,`Time` varchar(20)
,`Subject` varchar(30)
);
-- --------------------------------------------------------

--
-- Table structure for table `attendance`
--

CREATE TABLE IF NOT EXISTS `attendance` (
  `no` int(3) NOT NULL AUTO_INCREMENT,
  `Name` varchar(20) NOT NULL,
  `course` varchar(30) NOT NULL,
  `day` varchar(20) NOT NULL,
  `time` varchar(20) NOT NULL,
  `Presentday` int(11) NOT NULL,
  `Totalday` int(11) NOT NULL DEFAULT '30',
  PRIMARY KEY (`no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE IF NOT EXISTS `contact` (
  `No` int(3) NOT NULL AUTO_INCREMENT,
  `Name` varchar(15) NOT NULL,
  `email` varchar(100) NOT NULL,
  `mess` varchar(300) NOT NULL,
  PRIMARY KEY (`No`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=53 ;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`No`, `Name`, `email`, `mess`) VALUES
(22, 'Aryan', 'aryansoni0912@gmail.com', 'Hello '),
(24, 'zankhesh', 'zankheshparmar1510@gmail.com', 'Hiii'),
(42, 'ami', 'amisoni14111008@gmail.com', 'hello'),
(43, 'aryan', 'aryansoni0912@gmail.com', 'Hello , i am interested in python.'),
(44, 'ami', 'amisoni141197@gmail.com', 'Hello'),
(45, 'prapti', 'praptikachhia1908@gmail.com', 'hello...........'),
(46, 'Prapti', 'praptikachhia1908@gmail.com', 'hi'),
(47, 'cvsg', 'aryan.soni1209@gmail.com', 'hello'),
(48, 'cvsg', 'aryan.soni1209@gmail.com', 'gvcg'),
(49, 'kv;s', 'aryan.soni1209@gmail.com', 'kkl'),
(50, 'aa', 'aryan.soni1209@gmail.com', 'aaaa'),
(51, 'cvsg', 'aryan.soni1209@gmail.com', '23sswews'),
(52, 'aa', 'aryan.soni1209@gmail.com', 'aaa');

-- --------------------------------------------------------

--
-- Table structure for table `course`
--

CREATE TABLE IF NOT EXISTS `course` (
  `no` int(11) NOT NULL AUTO_INCREMENT,
  `img` varchar(50) NOT NULL,
  `Course_Name` varchar(20) NOT NULL,
  `by` varchar(30) NOT NULL,
  `date` date NOT NULL,
  `info` varchar(200) NOT NULL,
  PRIMARY KEY (`no`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `course`
--

INSERT INTO `course` (`no`, `img`, `Course_Name`, `by`, `date`, `info`) VALUES
(1, '1.jpg', 'C', 'Rs.8000', '2021-02-10', '2 Month'),
(2, '2.jpg', 'JAVA', 'RS.20000', '2021-02-10', '6 Month'),
(3, '3.jpg', 'Dot Net', 'Mr. Zankhesh', '2021-03-27', 'Basic, Adv.Dotnet'),
(4, '2.jpg', 'Excel', 'Mr. Zankhesh', '2021-03-13', 'Excel, Adv.Excel');

-- --------------------------------------------------------

--
-- Stand-in structure for view `datas`
--
CREATE TABLE IF NOT EXISTS `datas` (
`No` int(5)
,`course` varchar(50)
,`images` varchar(200)
,`sub_name` varchar(30)
,`date` varchar(50)
,`price` varchar(200)
,`content_info` varchar(100)
,`professorby` varchar(20)
);
-- --------------------------------------------------------

--
-- Table structure for table `faculty`
--

CREATE TABLE IF NOT EXISTS `faculty` (
  `no` int(10) NOT NULL,
  `Faculty_ID` int(15) NOT NULL,
  `Faculty_FName` varchar(10) NOT NULL,
  `Faculty_LName` varchar(10) NOT NULL,
  `Faculty_Contact` int(10) NOT NULL,
  `Faculty_Gender` varchar(6) NOT NULL,
  `Faculty_Add` varchar(30) NOT NULL,
  `Faculty_DOB` date NOT NULL,
  `Faculty_Sub` varchar(10) NOT NULL,
  `Faculty_Experience` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `marks`
--

CREATE TABLE IF NOT EXISTS `marks` (
  `No` int(11) NOT NULL AUTO_INCREMENT,
  `Stu_name` varchar(100) NOT NULL,
  `day` varchar(20) NOT NULL,
  `time` varchar(30) NOT NULL,
  `Sub_Name` varchar(30) NOT NULL,
  `Stu_Marks` int(11) NOT NULL,
  `totalmarks` int(11) NOT NULL,
  `Status` varchar(11) NOT NULL,
  PRIMARY KEY (`No`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=7 ;

--
-- Dumping data for table `marks`
--

INSERT INTO `marks` (`No`, `Stu_name`, `day`, `time`, `Sub_Name`, `Stu_Marks`, `totalmarks`, `Status`) VALUES
(4, 'prapti.v.kachhia', 'Thursday', '3:30-5', 'Dot Net', 50, 70, ''),
(5, 'meet.mukeshbhai.patel', 'wednesday', '3:30-5', 'Excel With Data Science', 60, 70, 'Pass'),
(6, 'ami.girishbhai.soni', 'Monday', '9-12', 'C', 21, 21, 'Pass');

-- --------------------------------------------------------

--
-- Table structure for table `news`
--

CREATE TABLE IF NOT EXISTS `news` (
  `No` int(10) NOT NULL AUTO_INCREMENT,
  `image` varchar(100) NOT NULL,
  `Name` varchar(15) NOT NULL,
  `date` date NOT NULL,
  `info` varchar(300) NOT NULL,
  PRIMARY KEY (`No`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `news`
--

INSERT INTO `news` (`No`, `image`, `Name`, `date`, `info`) VALUES
(1, '2.jpg', 'ARYAN', '2012-02-13', 'We are very excited to announce that ARYAN has successfully complete the Course of python. now he is Python certified developer. and placed id good company. All The Best Aryan'),
(2, '1.jpg', 'DHARA', '2021-02-17', 'We are very excited to announce that DHARA has successfully complete the Course of python. now he is JAVA certified developer. and placed id good company. All The Best DHARA\r\n');

-- --------------------------------------------------------

--
-- Table structure for table `registration`
--

CREATE TABLE IF NOT EXISTS `registration` (
  `No` int(5) NOT NULL AUTO_INCREMENT,
  `Email_id` varchar(100) NOT NULL,
  `Contact` text NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Password` varchar(30) NOT NULL,
  `Mname` varchar(50) NOT NULL,
  `lname` varchar(30) NOT NULL,
  `gender` varchar(11) NOT NULL,
  `bdate` date NOT NULL,
  `course` varchar(50) NOT NULL,
  `address` varchar(300) NOT NULL,
  `img` varchar(250) NOT NULL,
  PRIMARY KEY (`No`),
  UNIQUE KEY `Email_id` (`Email_id`),
  UNIQUE KEY `Email_id_2` (`Email_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=57 ;

--
-- Dumping data for table `registration`
--

INSERT INTO `registration` (`No`, `Email_id`, `Contact`, `Name`, `Password`, `Mname`, `lname`, `gender`, `bdate`, `course`, `address`, `img`) VALUES
(50, 'amisoni141197@gmail.com', '9275541389', 'ami', 'ami@1411', 'girishbhai', 'soni', 'F', '2021-03-17', 'JAVA', 'pune', ''),
(52, 'aryan.soni1209@gmail.com', '7894561230', 'aryan', '123', 'girishbhai', 'soni', 'M', '2021-03-03', 'Dot Net', 'ahmedavad', ''),
(53, 'meetp295@gmail.com', '985555555', 'meet', '88888', 'mukeshbhai', 'patel', 'M', '2021-03-05', 'C', 'AHMEDABAD', ''),
(54, 'prapti@gmail.com', '8488820837', 'prapti', '1234567890', 'v', 'kachhia', 'M', '2021-03-18', 'JAVA', 'isanpur', ''),
(55, 'praptikachhia1908@gmail.com', '8488820837', 'Prapti', 'pv@456', 'Vijaybhai', 'Kachhia', 'F', '2021-03-26', 'C', 'Isanpur', ''),
(56, 'aryansoni0912@gmail.com', '789461230', 'Aryan', 'aryan@123', 'Girishbhai', 'Soni', 'M', '0000-00-00', 'JAVA', 'Ahmedabad', '');

-- --------------------------------------------------------

--
-- Table structure for table `skill`
--

CREATE TABLE IF NOT EXISTS `skill` (
  `No` int(10) NOT NULL AUTO_INCREMENT,
  `1` varchar(30) NOT NULL DEFAULT '',
  `2` varchar(30) NOT NULL,
  `3` varchar(30) NOT NULL,
  `4` varchar(30) NOT NULL,
  `5` varchar(30) NOT NULL,
  `6` varchar(30) NOT NULL,
  `7` varchar(30) NOT NULL,
  `8` varchar(30) NOT NULL,
  PRIMARY KEY (`No`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `skill`
--

INSERT INTO `skill` (`No`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`) VALUES
(5, '75%', '80%', '45%', '70%', '20%', '35%', '48%', '56%');

-- --------------------------------------------------------

--
-- Table structure for table `subject`
--

CREATE TABLE IF NOT EXISTS `subject` (
  `No` int(5) NOT NULL AUTO_INCREMENT,
  `images` varchar(200) NOT NULL,
  `sub_name` varchar(30) NOT NULL,
  `professorby` varchar(20) NOT NULL,
  `date` varchar(50) NOT NULL,
  `price` varchar(200) NOT NULL,
  `content_info` varchar(100) NOT NULL,
  PRIMARY KEY (`No`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=10 ;

--
-- Dumping data for table `subject`
--

INSERT INTO `subject` (`No`, `images`, `sub_name`, `professorby`, `date`, `price`, `content_info`) VALUES
(1, '1.jpg', 'C', 'Mr.Vishal', '2 Month', 'RS.3000', 'Basic Of c , Adv.c '),
(2, '2.jpg', 'JAVA', 'Ms. Ami Soni', '6 Month', 'RS.15000', 'Basic, Adv.java'),
(3, '3.jpg', 'Dot Net', 'Mr. Zankhesh', '3 Month', 'RS.15000', 'BAsic, Adv.Dotnet'),
(9, '4.jpg', 'Excel With Data Science', 'Dhara Chapaneriya', '3 Months', '10000', 'basic Excel and excel With Data Science');

-- --------------------------------------------------------

--
-- Table structure for table `teacher`
--

CREATE TABLE IF NOT EXISTS `teacher` (
  `No` int(5) NOT NULL AUTO_INCREMENT,
  `img` varchar(200) NOT NULL,
  `Name` varchar(20) NOT NULL,
  `info` varchar(200) NOT NULL,
  `password` varchar(20) NOT NULL,
  `status` varchar(20) NOT NULL DEFAULT 'Active',
  PRIMARY KEY (`No`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=8 ;

--
-- Dumping data for table `teacher`
--

INSERT INTO `teacher` (`No`, `img`, `Name`, `info`, `password`, `status`) VALUES
(1, 'l-1.jpg', 'Mr. Vishal', 'C', '123456', 'Active'),
(2, 'l-4.jpg', 'Mr. Zankhesh', 'Dot Net', '123455', 'Active'),
(3, '3.jpg', 'Ami Soni', 'JAVA', '145', 'Active'),
(6, '2.jpg', 'Prapti', 'C', '123456', 'InActive'),
(7, '2.jpg', 'Kinjal', 'Dot Net', '123456789', 'Active');

-- --------------------------------------------------------

--
-- Table structure for table `timetable`
--

CREATE TABLE IF NOT EXISTS `timetable` (
  `no` int(3) NOT NULL AUTO_INCREMENT,
  `Lec_No` int(10) NOT NULL,
  `Time` varchar(20) NOT NULL,
  `Subject` varchar(30) NOT NULL,
  `Day` varchar(10) NOT NULL,
  PRIMARY KEY (`no`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=19 ;

--
-- Dumping data for table `timetable`
--

INSERT INTO `timetable` (`no`, `Lec_No`, `Time`, `Subject`, `Day`) VALUES
(3, 1, '1-3', 'JAVA', 'Tuesday'),
(8, 2, '3:30-5', 'C', 'Monday'),
(9, 3, '9-12', 'Dot Net', 'Monday'),
(18, 4, '1-3', 'Excel With Data Science', 'Monday');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE IF NOT EXISTS `user` (
  `No` int(3) NOT NULL AUTO_INCREMENT,
  `Name` varchar(15) NOT NULL,
  `password` varchar(20) NOT NULL,
  PRIMARY KEY (`No`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`No`, `Name`, `password`) VALUES
(5, 'admin', 'admin');

-- --------------------------------------------------------

--
-- Structure for view `attendace_detail`
--
DROP TABLE IF EXISTS `attendace_detail`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `attendace_detail` AS select `registration`.`No` AS `No`,`registration`.`Email_id` AS `Email_id`,`registration`.`Contact` AS `Contact`,`registration`.`Name` AS `Name`,`registration`.`Password` AS `Password`,`registration`.`Mname` AS `Mname`,`registration`.`lname` AS `lname`,`registration`.`gender` AS `gender`,`registration`.`bdate` AS `bdate`,`registration`.`course` AS `course`,`registration`.`address` AS `address`,`registration`.`img` AS `img`,`timetable`.`Day` AS `Day`,`timetable`.`Time` AS `Time`,`timetable`.`Subject` AS `Subject` from (`registration` left join `timetable` on((`registration`.`course` = `timetable`.`Subject`)));

-- --------------------------------------------------------

--
-- Structure for view `datas`
--
DROP TABLE IF EXISTS `datas`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `datas` AS select `registration`.`No` AS `No`,`registration`.`course` AS `course`,`subject`.`images` AS `images`,`subject`.`sub_name` AS `sub_name`,`subject`.`date` AS `date`,`subject`.`price` AS `price`,`subject`.`content_info` AS `content_info`,`subject`.`professorby` AS `professorby` from (`registration` left join `subject` on((`registration`.`course` = `subject`.`sub_name`)));

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
