-- phpMyAdmin SQL Dump
-- version 4.6.5.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 02, 2018 at 06:57 AM
-- Server version: 10.1.21-MariaDB
-- PHP Version: 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `affiliasicitedby`
--

-- --------------------------------------------------------

--
-- Table structure for table `searchget`
--

CREATE TABLE `searchget` (
  `citedby` varchar(50) NOT NULL,
  `affiliasi` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `searchget`
--

INSERT INTO `searchget` (`citedby`, `affiliasi`) VALUES
('27493', 'Stanford University'),
('3349', 'Rutgers University, New Brunswick, NJ');

-- --------------------------------------------------------

--
-- Table structure for table `searchpg`
--

CREATE TABLE `searchpg` (
  `citedby` varchar(50) NOT NULL,
  `affiliasi` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `searchpg`
--

INSERT INTO `searchpg` (`citedby`, `affiliasi`) VALUES
('27493', 'Stanford University'),
('3349', 'Rutgers University, New Brunswick, NJ');

-- --------------------------------------------------------

--
-- Table structure for table `searchpost`
--

CREATE TABLE `searchpost` (
  `citedby` varchar(50) NOT NULL,
  `affiliasi` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `searchpost`
--

INSERT INTO `searchpost` (`citedby`, `affiliasi`) VALUES
('27493', 'Stanford University'),
('3349', 'Rutgers University, New Brunswick, NJ');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `searchget`
--
ALTER TABLE `searchget`
  ADD PRIMARY KEY (`citedby`);

--
-- Indexes for table `searchpg`
--
ALTER TABLE `searchpg`
  ADD PRIMARY KEY (`citedby`);

--
-- Indexes for table `searchpost`
--
ALTER TABLE `searchpost`
  ADD PRIMARY KEY (`citedby`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
