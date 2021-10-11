-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 29, 2021 at 02:37 PM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 7.3.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_serveremail`
--

-- --------------------------------------------------------

--
-- Table structure for table `tb_client_mail`
--

CREATE TABLE `tb_client_mail` (
  `C_id` int(11) NOT NULL,
  `Fname` varchar(45) DEFAULT NULL,
  `Lname` varchar(45) DEFAULT NULL,
  `Email` varchar(45) DEFAULT NULL,
  `Gender` varchar(45) DEFAULT NULL,
  `isActive` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tb_client_mail`
--

INSERT INTO `tb_client_mail` (`C_id`, `Fname`, `Lname`, `Email`, `Gender`, `isActive`) VALUES
(14, 'fahad', 'alam', 'rjfahad44@gmail.com', 'Male', 1),
(15, 'sayem', 'hossian-1', 'md.sayemhossain.19@gmail.com', 'Male', 1),
(16, 'sayem', 'hossian-2', 'sayemawesome@gmail.com', 'Male', 1),
(17, 'sayem', 'hossian-3', 'sayemawasome@gmail.com', 'Male', 1);

-- --------------------------------------------------------

--
-- Table structure for table `tb_receiving_log`
--

CREATE TABLE `tb_receiving_log` (
  `id` int(11) NOT NULL,
  `DateTime` varchar(45) DEFAULT NULL,
  `To` varchar(45) DEFAULT NULL,
  `From` varchar(45) DEFAULT NULL,
  `Subject` varchar(45) DEFAULT NULL,
  `Body` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tb_receiving_log`
--

INSERT INTO `tb_receiving_log` (`id`, `DateTime`, `To`, `From`, `Subject`, `Body`) VALUES
(1, 'Date : March 24 2021, Time : 07:46:31 PM', 'Fahad Alam <rjfahad44@gmail.com>', 'Fahad2020Alam@gmail.com', 'Python', '\nTest abc cba\n\r\n');

-- --------------------------------------------------------

--
-- Table structure for table `tb_sending_log`
--

CREATE TABLE `tb_sending_log` (
  `id` int(11) NOT NULL,
  `DateTime` varchar(45) DEFAULT NULL,
  `From` varchar(45) DEFAULT NULL,
  `To` varchar(45) DEFAULT NULL,
  `Subject` varchar(45) DEFAULT NULL,
  `Body` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tb_sending_log`
--

INSERT INTO `tb_sending_log` (`id`, `DateTime`, `From`, `To`, `Subject`, `Body`) VALUES
(1, 'Date : March 24 2021, Time : 05:52:51 PM', 'Fahad2020Alam@gmail.com', 'md.sayemhossain.19@gmail.com', 'Test (24/03/2021)', '\nJust test purpose\n\r\n'),
(2, 'Date : March 24 2021, Time : 07:25:03 PM', 'Fahad2020Alam@gmail.com', 'rjfahad44@gmail.com', 'Abc', '\nAbcdefghijkl\n\r\n'),
(3, 'Date : March 24 2021, Time : 07:33:42 PM', 'Fahad2020Alam@gmail.com', 'rjfahad44@gmail.com', 'A', '\nAhajaj\n\r\n'),
(4, 'Date : March 24 2021, Time : 07:46:31 PM', 'Fahad2020Alam@gmail.com', 'rjfahad44@gmail.com', 'Python', '\nTest abc cba\n\r\n');

-- --------------------------------------------------------

--
-- Table structure for table `tb_server_log`
--

CREATE TABLE `tb_server_log` (
  `id` int(11) NOT NULL,
  `log` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tb_server_mail`
--

CREATE TABLE `tb_server_mail` (
  `S_id` int(11) NOT NULL,
  `S_email` varchar(45) DEFAULT NULL,
  `S_password` varchar(45) DEFAULT NULL,
  `S_host` varchar(45) DEFAULT NULL,
  `S_port` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tb_server_mail`
--

INSERT INTO `tb_server_mail` (`S_id`, `S_email`, `S_password`, `S_host`, `S_port`) VALUES
(1, 'Fahad2020Alam@gmail.com', 'Fahad_2020_3', 'imap.gmail.com', '465');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tb_client_mail`
--
ALTER TABLE `tb_client_mail`
  ADD PRIMARY KEY (`C_id`);

--
-- Indexes for table `tb_receiving_log`
--
ALTER TABLE `tb_receiving_log`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tb_sending_log`
--
ALTER TABLE `tb_sending_log`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tb_server_log`
--
ALTER TABLE `tb_server_log`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tb_server_mail`
--
ALTER TABLE `tb_server_mail`
  ADD PRIMARY KEY (`S_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tb_client_mail`
--
ALTER TABLE `tb_client_mail`
  MODIFY `C_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `tb_receiving_log`
--
ALTER TABLE `tb_receiving_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tb_sending_log`
--
ALTER TABLE `tb_sending_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `tb_server_log`
--
ALTER TABLE `tb_server_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tb_server_mail`
--
ALTER TABLE `tb_server_mail`
  MODIFY `S_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
