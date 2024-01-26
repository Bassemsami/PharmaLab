-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jan 20, 2024 at 01:06 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `MiceProj`
--

-- --------------------------------------------------------

--
-- Table structure for table `bridgePM`
--

CREATE TABLE `bridgePM` (
  `projectid` int(11) NOT NULL,
  `mouseid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `bridgeUP`
--

CREATE TABLE `bridgeUP` (
  `projectid` int(11) NOT NULL,
  `userid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `calculation`
--

CREATE TABLE `calculation` (
  `id` int(11) NOT NULL,
  `mouseID` int(11) NOT NULL,
  `projectID` int(11) NOT NULL,
  `pixels` double NOT NULL,
  `date` date NOT NULL,
  `createdby` int(255) NOT NULL,
  `percentage` int(11) NOT NULL,
  `day` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `calculation`
--

INSERT INTO `calculation` (`id`, `mouseID`, `projectID`, `pixels`, `date`, `createdby`, `percentage`, `day`) VALUES
(94, 7, 11, 1.023, '2024-01-18', 2, 0, 1),
(95, 7, 11, 0.679, '2024-01-18', 2, 34, 2),
(101, 7, 11, 0.581, '2024-01-18', 2, 43, 3),
(102, 7, 11, 0.063, '2024-01-19', 2, 94, 5),
(103, 7, 11, 0.162, '2024-01-19', 2, 84, 4),
(105, 14, 11, 0.721, '2024-01-19', 2, 0, 1),
(106, 14, 11, 0.597, '2024-01-19', 2, 17, 2);

-- --------------------------------------------------------

--
-- Table structure for table `mouse`
--

CREATE TABLE `mouse` (
  `mouseID` int(11) NOT NULL,
  `mouseName` varchar(255) NOT NULL,
  `project` int(255) NOT NULL,
  `createdby` int(255) NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `mouse`
--

INSERT INTO `mouse` (`mouseID`, `mouseName`, `project`, `createdby`, `date`) VALUES
(7, 'C1R', 11, 2, '2024-01-12'),
(14, 'C2R', 11, 2, '2024-01-18'),
(15, 'C1L', 11, 2, '2024-01-19'),
(17, 'MH1', 13, 22, '2024-01-20');

-- --------------------------------------------------------

--
-- Stand-in structure for view `mousecalculations`
-- (See below for the actual view)
--
CREATE TABLE `mousecalculations` (
`mouseName` varchar(255)
,`id` int(11)
,`mouseID` int(11)
,`projectID` int(11)
,`pixels` double
,`date` date
,`createdby` int(255)
,`percentage` int(11)
,`day` int(255)
);

-- --------------------------------------------------------

--
-- Table structure for table `project`
--

CREATE TABLE `project` (
  `ID` int(11) NOT NULL,
  `projectname` varchar(255) NOT NULL,
  `createddate` date NOT NULL,
  `createdby` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `project`
--

INSERT INTO `project` (`ID`, `projectname`, `createddate`, `createdby`) VALUES
(11, 'Echinecea', '2024-01-12', 2),
(13, 'Lab1', '2024-01-20', 22);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `ID` int(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `organisationname` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`ID`, `name`, `email`, `organisationname`, `password`) VALUES
(1, 'John Doe', 'johndoe@example.com', 'Acme Corp', '123456');

-- --------------------------------------------------------

--
-- Structure for view `mousecalculations`
--
DROP TABLE IF EXISTS `mousecalculations`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `miceproj`.`mousecalculations`  AS SELECT `m`.`mouseName` AS `mouseName`, `c`.`id` AS `id`, `c`.`mouseID` AS `mouseID`, `c`.`projectID` AS `projectID`, `c`.`pixels` AS `pixels`, `c`.`date` AS `date`, `c`.`createdby` AS `createdby`, `c`.`percentage` AS `percentage`, `c`.`day` AS `day` FROM (`miceproj`.`calculation` `c` join `miceproj`.`mouse` `m` on(`c`.`mouseID` = `m`.`mouseID`)) ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bridgePM`
--
ALTER TABLE `bridgePM`
  ADD KEY `mouseid` (`mouseid`),
  ADD KEY `projectid` (`projectid`);

--
-- Indexes for table `bridgeUP`
--
ALTER TABLE `bridgeUP`
  ADD KEY `projectid` (`projectid`),
  ADD KEY `userid` (`userid`);

--
-- Indexes for table `calculation`
--
ALTER TABLE `calculation`
  ADD PRIMARY KEY (`id`),
  ADD KEY `createdby` (`createdby`),
  ADD KEY `mouseID` (`mouseID`),
  ADD KEY `projectID` (`projectID`);

--
-- Indexes for table `mouse`
--
ALTER TABLE `mouse`
  ADD PRIMARY KEY (`mouseID`),
  ADD KEY `createdby` (`createdby`),
  ADD KEY `project` (`project`);

--
-- Indexes for table `project`
--
ALTER TABLE `project`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `created by` (`createdby`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `calculation`
--
ALTER TABLE `calculation`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=107;

--
-- AUTO_INCREMENT for table `mouse`
--
ALTER TABLE `mouse`
  MODIFY `mouseID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `project`
--
ALTER TABLE `project`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `ID` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `bridgePM`
--
ALTER TABLE `bridgePM`
  ADD CONSTRAINT `bridgepm_ibfk_1` FOREIGN KEY (`mouseid`) REFERENCES `mouse` (`mouseID`),
  ADD CONSTRAINT `bridgepm_ibfk_2` FOREIGN KEY (`projectid`) REFERENCES `project` (`ID`);

--
-- Constraints for table `bridgeUP`
--
ALTER TABLE `bridgeUP`
  ADD CONSTRAINT `bridgeup_ibfk_1` FOREIGN KEY (`projectid`) REFERENCES `project` (`ID`),
  ADD CONSTRAINT `bridgeup_ibfk_2` FOREIGN KEY (`userid`) REFERENCES `user` (`ID`);

--
-- Constraints for table `calculation`
--
ALTER TABLE `calculation`
  ADD CONSTRAINT `calculation_ibfk_1` FOREIGN KEY (`createdby`) REFERENCES `user` (`ID`),
  ADD CONSTRAINT `calculation_ibfk_2` FOREIGN KEY (`mouseID`) REFERENCES `mouse` (`mouseID`),
  ADD CONSTRAINT `calculation_ibfk_3` FOREIGN KEY (`projectID`) REFERENCES `project` (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
