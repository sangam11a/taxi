-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 12, 2023 at 12:15 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `taxi`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `adminid` int(10) NOT NULL,
  `fullname` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`adminid`, `fullname`, `address`, `email`, `password`) VALUES
(1, 'Nikita Thapa', 'Bhaktapur', 'nikita@gmail.com', '1234');

-- --------------------------------------------------------

--
-- Table structure for table `booking`
--

CREATE TABLE `booking` (
  `booking_id` int(10) NOT NULL,
  `pickup_address` varchar(100) DEFAULT NULL,
  `dropoff_address` varchar(100) DEFAULT NULL,
  `pickup_date` varchar(100) DEFAULT NULL,
  `pickup_time` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `cid` int(10) DEFAULT NULL,
  `did` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `booking`
--

INSERT INTO `booking` (`booking_id`, `pickup_address`, `dropoff_address`, `pickup_date`, `pickup_time`, `status`, `cid`, `did`) VALUES
(1, 'ktm', 'jhapa', '12/18/22', '12', 'Completed', 5, 1),
(6, 'chitwan', 'ktm', '12/24/22', '1 pm', 'Completed', 5, 1),
(8, 'ktm', 'jhapa', '1/4/23', '12', 'Completed', 11, 1),
(9, 'KTM', 'BKT', '1/4/23', '1 PM', 'Completed', 12, 4),
(10, 'asdfg', 'ghjk', '1/5/23', '12', 'Confirmed', 5, 6),
(11, 'ktm', 'bkt', '1/11/23', '1', 'Confirmed', 12, 5),
(12, 'bkt', 'jhapa', '1/5/23', '1pm', 'Confirmed', 12, 3),
(13, 'Bhaktapur', 'Kathmandu', '1/12/23', '12:00pm', 'Confirmed', 13, 2),
(14, 'Bhaktapur', 'Kathmandu', '1/12/23', '12:00pm', 'Confirmed', 13, 7),
(15, 'Bkt', 'Kathmandu', '1/12/23', '12:00pm', 'Confirmed', 13, 1),
(16, 'jj', 'ww', '1/5/23', '1', 'Confirmed', 13, 4),
(18, '', '', '1/7/23', '', 'Pending', 16, NULL),
(21, 'Bhaktapur', 'Kathmandu', '1/11/23', '1:00 pm', 'Completed', 18, 8),
(22, 'jhapa', 'Chitwan', '1/12/23', '1:00 pm ', 'Completed', 20, 14),
(23, 'pokhara', 'Chitwan', '1/12/23', '1:00 pm ', 'Confirmed', 20, 12);

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `cus_id` int(10) NOT NULL,
  `cus_name` varchar(100) NOT NULL,
  `cus_address` varchar(100) NOT NULL,
  `cus_email` varchar(100) NOT NULL,
  `cus_phone` varchar(15) NOT NULL,
  `cus_username` varchar(100) NOT NULL,
  `cus_password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`cus_id`, `cus_name`, `cus_address`, `cus_email`, `cus_phone`, `cus_username`, `cus_password`) VALUES
(5, 'nikita thapa', 'bkt', 'ad', 'nikita@gmail.co', 'ad', 'ad'),
(6, 'Nikita Thapa', 'Bhaktapur', '+977 9818125671', 'Nikita1@gmail.c', 'Nikita@123', 'Nikita@123'),
(7, 'Nikita Thapa', 'Bhaktapur', '+977 9818125671', 'Nikita1@gmail.c', 'Nikita@123', 'Nikita@123'),
(8, 'Nikesh Thapa', 'Ktm', '+977 9812748321', 'Nikesh1@gmail.c', 'Nikesh@12', 'Nikesh@12'),
(11, 'Nitesh hamal', 'Jhapa', 'nitesh@gmail.com', '+977 9813371345', 'Nitesh@123', 'Nitesh@123'),
(12, 'Sweecha Basnet', 'jhapa', 'Sweecha1@gmail.com', '+977 9812352728', 'Sweecha@1', 'Sweecha@1'),
(13, 'Nikita Thapa', 'Bhaktapur', 'Nikita1@gmail.com', '+977 9808946072', 'Nikita1', 'Nikita@1'),
(14, 'Nikita Thapa', 'Bkt', 'Nikita7@gmail.com', '+977 9812345678', 'Nikita1', 'Nikita@1'),
(15, 'Neuve Limbu', 'Jhapa', 'Neuve@gmail.com', '+977 9876123456', 'Neuve1', 'Neuve@12'),
(16, 'Pratik Neupane', 'Ktm', 'Pratik3@gmail.com', '+977 9812451612', 'Pratik@1', 'Pratik@1'),
(17, 'Mahesh Thapa', 'Banepa', 'Mahesh1@gmail.com', '+977 9812345678', 'Mahesh@1', 'Mahesh@1'),
(18, 'Tina Thapa', 'Jhapa', 'Tina1@gmail.com', '+977 9872415678', 'Tina@1', 'Tina@123'),
(19, 'Tina Thapa', 'Jhapa', 'Tina@gmail.com', '+977 9241678919', 'Tina@1', 'Tina@123'),
(20, 'Suprasidha subedi', 'Boudha', 'Suprasidhha@gmail.com', '+977 9812555431', 'Suprey@1', 'Suprey@1');

-- --------------------------------------------------------

--
-- Table structure for table `driver`
--

CREATE TABLE `driver` (
  `driver_id` int(10) NOT NULL,
  `fullname` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `licenseno` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `driver`
--

INSERT INTO `driver` (`driver_id`, `fullname`, `address`, `email`, `licenseno`, `status`, `password`) VALUES
(1, 'Nitesh Hamal', 'Arundhara-9, Jhapa', 'nitesh0hamal@gmail.com', '123456789', 'Inactive', 'someone'),
(2, 'Hancie Phago', 'Jhapa', 'hancie@gmail.com', '8873837738', 'Inactive', '1234'),
(3, 'Dilasha Sapkota', 'bhaktapur', 'dilasha@gmail.com', '443345ttf5', 'Inactive', '1234'),
(4, 'Nishav Rayamaghi', 'Ktm', 'nishav@gmail.com', '7787-9999-8888-9090', 'Inactive', '123'),
(5, 'Nikesh Thapa', 'bhaktapur', 'Nikesh1@gmail.com', '1112-3422', 'Inactive', '1111'),
(6, 'ram thapa', 'bkt', 'ram@gmail.com', '11229-18181', 'Inactive', 'ram'),
(7, 'Ajay Kc', 'bkt', 'Ajay1@gmail.com', '112233-1918', 'Inactive', '1111'),
(8, 'Dharti Bimali', 'Jhapa', 'dharti@gmail.com', '9999-8888-6666-3342', 'Active', '1234'),
(12, 'Sweecha Basnet', 'Jhapa', 'Sweecha@gmail.com', '1122-11177', 'Inactive', '1111'),
(13, 'Loman Gurung', 'Kathmandu', 'Loman@gmail.com', '112-009887', 'Active', '1111'),
(14, 'Suprasidha subedi', 'Kupondole', 'Suprey@gmail.com', '11190-6666', 'Active', '1111');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`adminid`);

--
-- Indexes for table `booking`
--
ALTER TABLE `booking`
  ADD PRIMARY KEY (`booking_id`),
  ADD KEY `cid` (`cid`),
  ADD KEY `did` (`did`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`cus_id`);

--
-- Indexes for table `driver`
--
ALTER TABLE `driver`
  ADD PRIMARY KEY (`driver_id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `licenseno` (`licenseno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `adminid` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `booking`
--
ALTER TABLE `booking`
  MODIFY `booking_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `cus_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `driver`
--
ALTER TABLE `driver`
  MODIFY `driver_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `booking`
--
ALTER TABLE `booking`
  ADD CONSTRAINT `booking_ibfk_1` FOREIGN KEY (`cid`) REFERENCES `customer` (`cus_id`),
  ADD CONSTRAINT `booking_ibfk_2` FOREIGN KEY (`did`) REFERENCES `driver` (`driver_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
