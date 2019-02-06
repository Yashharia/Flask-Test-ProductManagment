-- phpMyAdmin SQL Dump
-- version 4.8.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 06, 2019 at 04:58 PM
-- Server version: 10.1.34-MariaDB
-- PHP Version: 5.6.37

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `flaskapp`
--

-- --------------------------------------------------------

--
-- Table structure for table `location`
--

CREATE TABLE `location` (
  `location_id` varchar(55) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `location`
--

INSERT INTO `location` (`location_id`) VALUES
('Delhi'),
('MP'),
('Mumbai'),
('Odisha');

-- --------------------------------------------------------

--
-- Table structure for table `productmovement`
--

CREATE TABLE `productmovement` (
  `movement_id` int(11) NOT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `from_location` varchar(55) DEFAULT NULL,
  `to_location` varchar(55) DEFAULT NULL,
  `product_id` varchar(55) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `productmovement`
--

INSERT INTO `productmovement` (`movement_id`, `time`, `from_location`, `to_location`, `product_id`, `quantity`) VALUES
(1, '2019-02-06 08:00:14', 'Delhi', 'null', 'P1', 5),
(2, '2019-02-06 09:12:23', 'null', 'Mumbai', 'P1', 55),
(3, '2019-02-06 09:12:28', 'Mumbai', 'Delhi', 'P3', 25),
(4, '2019-02-06 10:25:41', 'Mumbai', 'Delhi', 'p25', 10),
(5, '2019-02-06 15:56:04', 'Delhi', 'Odisha', 'p45', 2);

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `product_id` varchar(55) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`product_id`) VALUES
('P1'),
('p20'),
('p25'),
('P3'),
('p32'),
('p45');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `location`
--
ALTER TABLE `location`
  ADD PRIMARY KEY (`location_id`);

--
-- Indexes for table `productmovement`
--
ALTER TABLE `productmovement`
  ADD PRIMARY KEY (`movement_id`),
  ADD KEY `product_id` (`product_id`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`product_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `productmovement`
--
ALTER TABLE `productmovement`
  MODIFY `movement_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `productmovement`
--
ALTER TABLE `productmovement`
  ADD CONSTRAINT `productmovement_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
