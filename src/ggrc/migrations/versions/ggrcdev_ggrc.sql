-- MySQL dump 10.13  Distrib 5.5.47, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: ggrcdev
-- ------------------------------------------------------
-- Server version	5.5.47-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `access_groups`
--

DROP TABLE IF EXISTS `access_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `access_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `os_state` varchar(250) NOT NULL,
  `end_date` date DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `status` varchar(250) DEFAULT NULL,
  `notes` text,
  `description` text,
  `url` varchar(250) DEFAULT NULL,
  `reference_url` varchar(250) DEFAULT NULL,
  `secondary_contact_id` int(11) DEFAULT NULL,
  `contact_id` int(11) DEFAULT NULL,
  `title` varchar(250) NOT NULL,
  `slug` varchar(250) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `modified_by_id` int(11) DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `context_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_access_groups` (`slug`),
  UNIQUE KEY `uq_t_access_groups` (`title`),
  KEY `fk_access_groups_contact` (`contact_id`),
  KEY `fk_access_groups_contexts` (`context_id`),
  KEY `fk_access_groups_secondary_contact` (`secondary_contact_id`),
  KEY `ix_access_groups_updated_at` (`updated_at`),
  CONSTRAINT `access_groups_ibfk_1` FOREIGN KEY (`contact_id`) REFERENCES `people` (`id`),
  CONSTRAINT `access_groups_ibfk_2` FOREIGN KEY (`context_id`) REFERENCES `contexts` (`id`),
  CONSTRAINT `access_groups_ibfk_3` FOREIGN KEY (`secondary_contact_id`) REFERENCES `people` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `access_groups`
--

LOCK TABLES `access_groups` WRITE;
/*!40000 ALTER TABLE `access_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `access_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `audit_objects`
--

DROP TABLE IF EXISTS `audit_objects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `audit_objects` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `modified_by_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `context_id` int(11) NOT NULL,
  `audit_id` int(11) NOT NULL,
  `auditable_id` int(11) NOT NULL,
  `auditable_type` varchar(250) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `audit_id` (`audit_id`,`auditable_id`,`auditable_type`),
  KEY `context_id` (`context_id`),
  CONSTRAINT `audit_objects_ibfk_1` FOREIGN KEY (`context_id`) REFERENCES `contexts` (`id`),
  CONSTRAINT `audit_objects_ibfk_2` FOREIGN KEY (`audit_id`) REFERENCES `audits` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `audit_objects`
--

LOCK TABLES `audit_objects` WRITE;
/*!40000 ALTER TABLE `audit_objects` DISABLE KEYS */;
/*!40000 ALTER TABLE `audit_objects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `audits`
--

DROP TABLE IF EXISTS `audits`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `audits` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(250) NOT NULL,
  `slug` varchar(250) NOT NULL,
  `description` text,
  `url` varchar(250) DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `report_start_date` date DEFAULT NULL,
  `report_end_date` date DEFAULT NULL,
  `contact_id` int(11) DEFAULT NULL,
  `status` enum('Planned','In Progress','Manager Review','Ready for External Review','Completed') NOT NULL,
  `gdrive_evidence_folder` varchar(250) DEFAULT NULL,
  `program_id` int(11) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `modified_by_id` int(11) DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `context_id` int(11) DEFAULT NULL,
  `notes` text,
  `audit_firm_id` int(11) DEFAULT NULL,
  `reference_url` varchar(250) DEFAULT NULL,
  `object_type` varchar(250) NOT NULL,
  `secondary_contact_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_t_audits` (`title`),
  KEY `program_id` (`program_id`),
  KEY `fk_audits_contact` (`contact_id`),
  KEY `fk_audits_contexts` (`context_id`),
  KEY `ix_audits_updated_at` (`updated_at`),
  KEY `fk_audits_secondary_contact` (`secondary_contact_id`),
  CONSTRAINT `audits_ibfk_1` FOREIGN KEY (`context_id`) REFERENCES `contexts` (`id`),
  CONSTRAINT `audits_ibfk_3` FOREIGN KEY (`program_id`) REFERENCES `programs` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `audits`
--

LOCK TABLES `audits` WRITE;
/*!40000 ALTER TABLE `audits` DISABLE KEYS */;
/*!40000 ALTER TABLE `audits` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `background_tasks`
--

DROP TABLE IF EXISTS `background_tasks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `background_tasks` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(250) DEFAULT NULL,
  `parameters` mediumblob,
  `result` mediumblob,
  `created_at` datetime DEFAULT NULL,
  `modified_by_id` int(11) DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `context_id` int(11) DEFAULT NULL,
  `status` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_background_tasks_contexts` (`context_id`),
  KEY `ix_background_tasks_updated_at` (`updated_at`),
  CONSTRAINT `background_tasks_ibfk_1` FOREIGN KEY (`context_id`) REFERENCES `contexts` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `background_tasks`
--

LOCK TABLES `background_tasks` WRITE;
/*!40000 ALTER TABLE `background_tasks` DISABLE KEYS */;
/*!40000 ALTER TABLE `background_tasks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `calendar_entries`
--

DROP TABLE IF EXISTS `calendar_entries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `calendar_entries` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(250) DEFAULT NULL,
  `calendar_id` varchar(250) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `modified_by_id` int(11) DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `context_id` int(11) DEFAULT NULL,
  `owner_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `owner_id` (`owner_id`),
  KEY `fk_calendar_entries_contexts` (`context_id`),
  KEY `ix_calendar_entries_updated_at` (`updated_at`),
  CONSTRAINT `calendar_entries_ibfk_1` FOREIGN KEY (`context_id`) REFERENCES `contexts` (`id`),
  CONSTRAINT `calendar_entries_ibfk_2` FOREIGN KEY (`owner_id`) REFERENCES `people` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `calendar_entries`
--

LOCK TABLES `calendar_entries` WRITE;
/*!40000 ALTER TABLE `calendar_entries` DISABLE KEYS */;
/*!40000 ALTER TABLE `calendar_entries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `categories` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `modified_by_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `name` varchar(250) DEFAULT NULL,
  `lft` int(11) DEFAULT NULL,
  `rgt` int(11) DEFAULT NULL,
  `scope_id` int(11) DEFAULT NULL,
  `depth` int(11) DEFAULT NULL,
  `required` tinyint(1) DEFAULT NULL,
  `parent_id` int(11) DEFAULT NULL,
  `context_id` int(11) DEFAULT NULL,
  `type` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `parent_id` (`parent_id`),
  KEY `fk_categories_contexts` (`context_id`),
  KEY `ix_categories_updated_at` (`updated_at`),
  CONSTRAINT `fk_categories_contexts` FOREIGN KEY (`context_id`) REFERENCES `contexts` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=66 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categories`
--

LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` VALUES (37,NULL,'2016-05-03 10:37:03','2016-05-03 10:37:03','Confidentiality',NULL,NULL,102,NULL,NULL,NULL,NULL,'ControlAssertion'),(38,NULL,'2016-05-03 10:37:03','2016-05-03 10:37:03','Integrity',NULL,NULL,102,NULL,NULL,NULL,NULL,'ControlAssertion'),(39,NULL,'2016-05-03 10:37:03','2016-05-03 10:37:03','Availability',NULL,NULL,102,NULL,NULL,NULL,NULL,'ControlAssertion'),(40,NULL,'2016-05-03 10:37:03','2016-05-03 10:37:03','Security',NULL,NULL,102,NULL,NULL,NULL,NULL,'ControlAssertion'),(41,NULL,'2016-05-03 10:37:03','2016-05-03 10:37:03','Privacy',NULL,NULL,102,NULL,NULL,NULL,NULL,'ControlAssertion'),(42,NULL,'2016-05-03 10:37:03','2016-05-03 10:37:03','Org and Admin/Governance',NULL,NULL,100,NULL,NULL,NULL,NULL,'ControlCategory'),(43,NULL,'2016-05-03 10:37:03','2016-05-03 10:37:03','Training',NULL,NULL,100,NULL,NULL,NULL,NULL,'ControlCategory'),(44,NULL,'2016-05-03 10:37:03','2016-05-03 10:37:03','Policies & Procedures',NULL,NULL,100,NULL,NULL,NULL,NULL,'ControlCategory'),(45,NULL,'2016-05-03 10:37:03','2016-05-03 10:37:03','HR',NULL,NULL,100,NULL,NULL,NULL,NULL,'ControlCategory'),(46,NULL,'2016-05-03 10:37:03','2016-05-03 10:37:03','Logical Access/ Access Control',NULL,NULL,100,NULL,NULL,NULL,NULL,'ControlCategory'),(47,NULL,'2016-05-03 10:37:03','2016-05-03 10:37:03','Access Management',NULL,NULL,100,NULL,NULL,NULL,NULL,'ControlCategory'),(48,NULL,'2016-05-03 10:37:03','2016-05-03 10:37:03','Authorization',NULL,NULL,100,NULL,NULL,NULL,NULL,'ControlCategory'),(49,NULL,'2016-05-03 10:37:03','2016-05-03 10:37:03','Authentication',NULL,NULL,100,NULL,NULL,NULL,NULL,'ControlCategory'),(50,NULL,'2016-05-03 10:37:03','2016-05-03 10:37:03','Change Management',NULL,NULL,100,NULL,NULL,NULL,NULL,'ControlCategory'),(51,NULL,'2016-05-03 10:37:03','2016-05-03 10:37:03','Segregation of Duties',NULL,NULL,100,NULL,NULL,NULL,NULL,'ControlCategory'),(52,NULL,'2016-05-03 10:37:03','2016-05-03 10:37:03','Configuration Management',NULL,NULL,100,NULL,NULL,NULL,NULL,'ControlCategory'),(53,NULL,'2016-05-03 10:37:03','2016-05-03 10:37:03','Package Verification and Code release',NULL,NULL,100,NULL,NULL,NULL,NULL,'ControlCategory'),(54,NULL,'2016-05-03 10:37:03','2016-05-03 10:37:03','Incident Management',NULL,NULL,100,NULL,NULL,NULL,NULL,'ControlCategory'),(55,NULL,'2016-05-03 10:37:03','2016-05-03 10:37:03','Monitoring ',NULL,NULL,100,NULL,NULL,NULL,NULL,'ControlCategory'),(56,NULL,'2016-05-03 10:37:03','2016-05-03 10:37:03','Process',NULL,NULL,100,NULL,NULL,NULL,NULL,'ControlCategory'),(57,NULL,'2016-05-03 10:37:03','2016-05-03 10:37:03','Business Continuity',NULL,NULL,100,NULL,NULL,NULL,NULL,'ControlCategory'),(58,NULL,'2016-05-03 10:37:03','2016-05-03 10:37:03','Disaster Recovery',NULL,NULL,100,NULL,NULL,NULL,NULL,'ControlCategory'),(59,NULL,'2016-05-03 10:37:03','2016-05-03 10:37:03','Restoration Tests',NULL,NULL,100,NULL,NULL,NULL,NULL,'ControlCategory'),(60,NULL,'2016-05-03 10:37:03','2016-05-03 10:37:03','Backup Logs ',NULL,NULL,100,NULL,NULL,NULL,NULL,'ControlCategory'),(61,NULL,'2016-05-03 10:37:03','2016-05-03 10:37:03','Replication',NULL,NULL,100,NULL,NULL,NULL,NULL,'ControlCategory'),(62,NULL,'2016-05-03 10:37:03','2016-05-03 10:37:03','Data Protection and Retention',NULL,NULL,100,NULL,NULL,NULL,NULL,'ControlCategory'),(63,NULL,'2016-05-03 10:37:03','2016-05-03 10:37:03','Physical Security',NULL,NULL,100,NULL,NULL,NULL,NULL,'ControlCategory'),(64,NULL,'2016-05-03 10:37:03','2016-05-03 10:37:03','Data Centers',NULL,NULL,100,NULL,NULL,NULL,NULL,'ControlCategory'),(65,NULL,'2016-05-03 10:37:03','2016-05-03 10:37:03','Sites',NULL,NULL,100,NULL,NULL,NULL,NULL,'ControlCategory');
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categorizations`
--

DROP TABLE IF EXISTS `categorizations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `categorizations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `modified_by_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `category_id` int(11) NOT NULL,
  `categorizable_id` int(11) DEFAULT NULL,
  `categorizable_type` varchar(250) DEFAULT NULL,
  `context_id` int(11) DEFAULT NULL,
  `category_type` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `category_id` (`category_id`),
  KEY `fk_categorizations_contexts` (`context_id`),
  KEY `ix_categorizations_updated_at` (`updated_at`),
  CONSTRAINT `categorizations_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`),
  CONSTRAINT `fk_categorizations_contexts` FOREIGN KEY (`context_id`) REFERENCES `contexts` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categorizations`
--

LOCK TABLES `categorizations` WRITE;
/*!40000 ALTER TABLE `categorizations` DISABLE KEYS */;
/*!40000 ALTER TABLE `categorizations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clauses`
--

DROP TABLE IF EXISTS `clauses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `clauses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `na` tinyint(1) NOT NULL,
  `notes` text,
  `os_state` varchar(250) NOT NULL,
  `parent_id` int(11) DEFAULT NULL,
  `description` text,
  `url` varchar(250) DEFAULT NULL,
  `reference_url` varchar(250) DEFAULT NULL,
  `secondary_contact_id` int(11) DEFAULT NULL,
  `contact_id` int(11) DEFAULT NULL,
  `title` varchar(250) NOT NULL,
  `slug` varchar(250) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `modified_by_id` int(11) DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `context_id` int(11) DEFAULT NULL,
  `status` varchar(250) DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_clauses` (`slug`),
  UNIQUE KEY `uq_t_clauses` (`title`),
  KEY `contact_id` (`contact_id`),
  KEY `context_id` (`context_id`),
  KEY `parent_id` (`parent_id`),
  KEY `secondary_contact_id` (`secondary_contact_id`),
  CONSTRAINT `clauses_ibfk_1` FOREIGN KEY (`contact_id`) REFERENCES `people` (`id`),
  CONSTRAINT `clauses_ibfk_2` FOREIGN KEY (`context_id`) REFERENCES `contexts` (`id`),
  CONSTRAINT `clauses_ibfk_3` FOREIGN KEY (`parent_id`) REFERENCES `clauses` (`id`),
  CONSTRAINT `clauses_ibfk_4` FOREIGN KEY (`secondary_contact_id`) REFERENCES `people` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clauses`
--

LOCK TABLES `clauses` WRITE;
/*!40000 ALTER TABLE `clauses` DISABLE KEYS */;
/*!40000 ALTER TABLE `clauses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `description` text,
  `created_at` datetime DEFAULT NULL,
  `modified_by_id` int(11) DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `context_id` int(11) DEFAULT NULL,
  `assignee_type` text,
  PRIMARY KEY (`id`),
  KEY `context_id` (`context_id`),
  CONSTRAINT `comments_ibfk_1` FOREIGN KEY (`context_id`) REFERENCES `contexts` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contexts`
--

DROP TABLE IF EXISTS `contexts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contexts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) DEFAULT NULL,
  `description` text,
  `related_object_id` int(11) DEFAULT NULL,
  `related_object_type` varchar(128) DEFAULT NULL,
  `modified_by_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `context_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_contexts_contexts` (`context_id`),
  KEY `ix_context_related_object` (`related_object_type`,`related_object_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contexts`
--

LOCK TABLES `contexts` WRITE;
/*!40000 ALTER TABLE `contexts` DISABLE KEYS */;
INSERT INTO `contexts` VALUES (1,'Administration','Context for Administrative resources.',NULL,NULL,0,NULL,NULL,1);
/*!40000 ALTER TABLE `contexts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `control_assessments`
--

DROP TABLE IF EXISTS `control_assessments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `control_assessments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `design` varchar(250) DEFAULT NULL,
  `operationally` varchar(250) DEFAULT NULL,
  `os_state` varchar(250) NOT NULL,
  `test_plan` text,
  `end_date` date DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `status` varchar(250) DEFAULT NULL,
  `notes` text,
  `description` text,
  `url` varchar(250) DEFAULT NULL,
  `reference_url` varchar(250) DEFAULT NULL,
  `secondary_contact_id` int(11) DEFAULT NULL,
  `contact_id` int(11) DEFAULT NULL,
  `title` varchar(250) NOT NULL,
  `slug` varchar(250) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `modified_by_id` int(11) DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `context_id` int(11) DEFAULT NULL,
  `control_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_control_assessments` (`slug`),
  UNIQUE KEY `uq_t_control_assessments` (`title`),
  KEY `contact_id` (`contact_id`),
  KEY `context_id` (`context_id`),
  KEY `secondary_contact_id` (`secondary_contact_id`),
  KEY `fk_control_control_assessment` (`control_id`),
  CONSTRAINT `fk_control_control_assessment` FOREIGN KEY (`control_id`) REFERENCES `controls` (`id`),
  CONSTRAINT `control_assessments_ibfk_1` FOREIGN KEY (`contact_id`) REFERENCES `people` (`id`),
  CONSTRAINT `control_assessments_ibfk_2` FOREIGN KEY (`context_id`) REFERENCES `contexts` (`id`),
  CONSTRAINT `control_assessments_ibfk_3` FOREIGN KEY (`secondary_contact_id`) REFERENCES `people` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `control_assessments`
--

LOCK TABLES `control_assessments` WRITE;
/*!40000 ALTER TABLE `control_assessments` DISABLE KEYS */;
/*!40000 ALTER TABLE `control_assessments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `control_controls`
--

DROP TABLE IF EXISTS `control_controls`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `control_controls` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `modified_by_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `control_id` int(11) NOT NULL,
  `implemented_control_id` int(11) NOT NULL,
  `context_id` int(11) DEFAULT NULL,
  `status` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_control_controls` (`control_id`,`implemented_control_id`),
  KEY `fk_control_controls_contexts` (`context_id`),
  KEY `ix_control_id` (`control_id`),
  KEY `ix_implemented_control_id` (`implemented_control_id`),
  KEY `ix_control_controls_updated_at` (`updated_at`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `control_controls`
--

LOCK TABLES `control_controls` WRITE;
/*!40000 ALTER TABLE `control_controls` DISABLE KEYS */;
/*!40000 ALTER TABLE `control_controls` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `control_sections`
--

DROP TABLE IF EXISTS `control_sections`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `control_sections` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `modified_by_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `control_id` int(11) NOT NULL,
  `section_id` int(11) NOT NULL,
  `context_id` int(11) DEFAULT NULL,
  `status` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_control_sections` (`control_id`,`section_id`),
  KEY `fk_control_sections_contexts` (`context_id`),
  KEY `ix_control_id` (`control_id`),
  KEY `ix_section_id` (`section_id`),
  KEY `ix_control_sections_updated_at` (`updated_at`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `control_sections`
--

LOCK TABLES `control_sections` WRITE;
/*!40000 ALTER TABLE `control_sections` DISABLE KEYS */;
/*!40000 ALTER TABLE `control_sections` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `controls`
--

DROP TABLE IF EXISTS `controls`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `controls` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `modified_by_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `description` text,
  `url` varchar(250) DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `slug` varchar(250) NOT NULL,
  `title` varchar(250) NOT NULL,
  `directive_id` int(11) DEFAULT NULL,
  `kind_id` int(11) DEFAULT NULL,
  `means_id` int(11) DEFAULT NULL,
  `version` varchar(250) DEFAULT NULL,
  `documentation_description` text,
  `verify_frequency_id` int(11) DEFAULT NULL,
  `fraud_related` tinyint(1) DEFAULT NULL,
  `key_control` tinyint(1) DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL,
  `notes` text,
  `parent_id` int(11) DEFAULT NULL,
  `company_control` tinyint(1) DEFAULT NULL,
  `context_id` int(11) DEFAULT NULL,
  `contact_id` int(11) DEFAULT NULL,
  `status` varchar(250) DEFAULT NULL,
  `principal_assessor_id` int(11) DEFAULT NULL,
  `secondary_assessor_id` int(11) DEFAULT NULL,
  `reference_url` varchar(250) DEFAULT NULL,
  `secondary_contact_id` int(11) DEFAULT NULL,
  `os_state` varchar(16) NOT NULL,
  `test_plan` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_controls` (`slug`),
  UNIQUE KEY `uq_t_controls` (`title`),
  KEY `directive_id` (`directive_id`),
  KEY `parent_id` (`parent_id`),
  KEY `fk_controls_contexts` (`context_id`),
  KEY `fk_controls_contact` (`contact_id`),
  KEY `ix_controls_principal_assessor` (`principal_assessor_id`),
  KEY `ix_controls_secondary_assessor` (`secondary_assessor_id`),
  KEY `ix_controls_updated_at` (`updated_at`),
  KEY `fk_controls_secondary_contact` (`secondary_contact_id`),
  CONSTRAINT `controls_ibfk_1` FOREIGN KEY (`directive_id`) REFERENCES `directives` (`id`),
  CONSTRAINT `controls_ibfk_2` FOREIGN KEY (`parent_id`) REFERENCES `controls` (`id`),
  CONSTRAINT `fk_controls_contexts` FOREIGN KEY (`context_id`) REFERENCES `contexts` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `controls`
--

LOCK TABLES `controls` WRITE;
/*!40000 ALTER TABLE `controls` DISABLE KEYS */;
/*!40000 ALTER TABLE `controls` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `custom_attribute_definitions`
--

DROP TABLE IF EXISTS `custom_attribute_definitions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `custom_attribute_definitions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `modified_by_id` int(11) DEFAULT NULL,
  `context_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `title` varchar(250) NOT NULL,
  `helptext` varchar(250) NOT NULL,
  `placeholder` varchar(250) DEFAULT NULL,
  `definition_type` varchar(250) NOT NULL,
  `attribute_type` varchar(250) NOT NULL,
  `multi_choice_options` text,
  `mandatory` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_custom_attributes_title` (`title`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `custom_attribute_definitions`
--

LOCK TABLES `custom_attribute_definitions` WRITE;
/*!40000 ALTER TABLE `custom_attribute_definitions` DISABLE KEYS */;
/*!40000 ALTER TABLE `custom_attribute_definitions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `custom_attribute_values`
--

DROP TABLE IF EXISTS `custom_attribute_values`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `custom_attribute_values` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `modified_by_id` int(11) DEFAULT NULL,
  `context_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `custom_attribute_id` int(11) NOT NULL,
  `attributable_id` int(11) DEFAULT NULL,
  `attributable_type` varchar(250) DEFAULT NULL,
  `attribute_value` text,
  PRIMARY KEY (`id`),
  KEY `custom_attribute_values_ibfk_1` (`custom_attribute_id`),
  KEY `ix_custom_attributes_attributable` (`attributable_id`,`attributable_type`),
  CONSTRAINT `custom_attribute_values_ibfk_1` FOREIGN KEY (`custom_attribute_id`) REFERENCES `custom_attribute_definitions` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `custom_attribute_values`
--

LOCK TABLES `custom_attribute_values` WRITE;
/*!40000 ALTER TABLE `custom_attribute_values` DISABLE KEYS */;
/*!40000 ALTER TABLE `custom_attribute_values` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `data_assets`
--

DROP TABLE IF EXISTS `data_assets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `data_assets` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `modified_by_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `description` text,
  `url` varchar(250) DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `slug` varchar(250) NOT NULL,
  `title` varchar(250) NOT NULL,
  `context_id` int(11) DEFAULT NULL,
  `contact_id` int(11) DEFAULT NULL,
  `notes` text,
  `status` varchar(250) DEFAULT NULL,
  `reference_url` varchar(250) DEFAULT NULL,
  `secondary_contact_id` int(11) DEFAULT NULL,
  `os_state` varchar(16) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_data_assets` (`slug`),
  UNIQUE KEY `uq_t_data_assets` (`title`),
  KEY `fk_data_assets_contexts` (`context_id`),
  KEY `fk_data_assets_contact` (`contact_id`),
  KEY `ix_data_assets_updated_at` (`updated_at`),
  KEY `fk_data_assets_secondary_contact` (`secondary_contact_id`),
  CONSTRAINT `fk_data_assets_contexts` FOREIGN KEY (`context_id`) REFERENCES `contexts` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `data_assets`
--

LOCK TABLES `data_assets` WRITE;
/*!40000 ALTER TABLE `data_assets` DISABLE KEYS */;
/*!40000 ALTER TABLE `data_assets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `directive_controls`
--

DROP TABLE IF EXISTS `directive_controls`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `directive_controls` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `modified_by_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `directive_id` int(11) NOT NULL,
  `control_id` int(11) NOT NULL,
  `context_id` int(11) DEFAULT NULL,
  `status` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_directive_controls` (`directive_id`,`control_id`),
  KEY `ix_directive_id` (`directive_id`),
  KEY `ix_control_id` (`control_id`),
  KEY `fk_directive_controls_contexts` (`context_id`),
  KEY `ix_directive_controls_updated_at` (`updated_at`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `directive_controls`
--

LOCK TABLES `directive_controls` WRITE;
/*!40000 ALTER TABLE `directive_controls` DISABLE KEYS */;
/*!40000 ALTER TABLE `directive_controls` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `directive_sections`
--

DROP TABLE IF EXISTS `directive_sections`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `directive_sections` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `directive_id` int(11) NOT NULL,
  `section_id` int(11) NOT NULL,
  `status` varchar(250) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `modified_by_id` int(11) DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `context_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `directive_id` (`directive_id`,`section_id`),
  KEY `section_id` (`section_id`),
  KEY `fk_directive_sections_contexts` (`context_id`),
  KEY `ix_directive_sections_updated_at` (`updated_at`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `directive_sections`
--

LOCK TABLES `directive_sections` WRITE;
/*!40000 ALTER TABLE `directive_sections` DISABLE KEYS */;
/*!40000 ALTER TABLE `directive_sections` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `directives`
--

DROP TABLE IF EXISTS `directives`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `directives` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `modified_by_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `description` text,
  `url` varchar(250) DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `slug` varchar(250) NOT NULL,
  `title` varchar(250) NOT NULL,
  `version` varchar(250) DEFAULT NULL,
  `organization` varchar(250) DEFAULT NULL,
  `scope` text,
  `kind_id` int(11) DEFAULT NULL,
  `audit_start_date` datetime DEFAULT NULL,
  `audit_frequency_id` int(11) DEFAULT NULL,
  `audit_duration_id` int(11) DEFAULT NULL,
  `kind` varchar(250) DEFAULT NULL,
  `context_id` int(11) DEFAULT NULL,
  `meta_kind` varchar(250) DEFAULT NULL,
  `contact_id` int(11) DEFAULT NULL,
  `notes` text,
  `status` varchar(250) DEFAULT NULL,
  `reference_url` varchar(250) DEFAULT NULL,
  `secondary_contact_id` int(11) DEFAULT NULL,
  `os_state` varchar(16) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_directives` (`slug`),
  UNIQUE KEY `uq_t_directives` (`title`),
  KEY `fk_directives_contexts` (`context_id`),
  KEY `fk_directives_contact` (`contact_id`),
  KEY `ix_directives_meta_kind` (`meta_kind`),
  KEY `ix_directives_updated_at` (`updated_at`),
  KEY `fk_directives_secondary_contact` (`secondary_contact_id`),
  CONSTRAINT `fk_directives_contexts` FOREIGN KEY (`context_id`) REFERENCES `contexts` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `directives`
--

LOCK TABLES `directives` WRITE;
/*!40000 ALTER TABLE `directives` DISABLE KEYS */;
/*!40000 ALTER TABLE `directives` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `documents`
--

DROP TABLE IF EXISTS `documents`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `documents` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `modified_by_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `title` varchar(250) DEFAULT NULL,
  `link` varchar(250) DEFAULT NULL,
  `description` text,
  `kind_id` int(11) DEFAULT NULL,
  `year_id` int(11) DEFAULT NULL,
  `language_id` int(11) DEFAULT NULL,
  `context_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_documents_contexts` (`context_id`),
  KEY `ix_documents_updated_at` (`updated_at`),
  CONSTRAINT `fk_documents_contexts` FOREIGN KEY (`context_id`) REFERENCES `contexts` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `documents`
--

LOCK TABLES `documents` WRITE;
/*!40000 ALTER TABLE `documents` DISABLE KEYS */;
/*!40000 ALTER TABLE `documents` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `events`
--

DROP TABLE IF EXISTS `events`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `events` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `modified_by_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `action` enum('POST','PUT','DELETE','IMPORT','GET') NOT NULL,
  `resource_id` int(11) DEFAULT NULL,
  `resource_type` varchar(250) DEFAULT NULL,
  `context_id` int(11) DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `events_modified_by` (`modified_by_id`),
  KEY `fk_events_contexts` (`context_id`),
  KEY `ix_events_updated_at` (`updated_at`),
  CONSTRAINT `events_modified_by` FOREIGN KEY (`modified_by_id`) REFERENCES `people` (`id`),
  CONSTRAINT `fk_events_contexts` FOREIGN KEY (`context_id`) REFERENCES `contexts` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `events`
--

LOCK TABLES `events` WRITE;
/*!40000 ALTER TABLE `events` DISABLE KEYS */;
/*!40000 ALTER TABLE `events` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `facilities`
--

DROP TABLE IF EXISTS `facilities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `facilities` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `modified_by_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `description` text,
  `url` varchar(250) DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `slug` varchar(250) NOT NULL,
  `title` varchar(250) NOT NULL,
  `context_id` int(11) DEFAULT NULL,
  `contact_id` int(11) DEFAULT NULL,
  `notes` text,
  `status` varchar(250) DEFAULT NULL,
  `reference_url` varchar(250) DEFAULT NULL,
  `secondary_contact_id` int(11) DEFAULT NULL,
  `os_state` varchar(16) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_facilities` (`slug`),
  UNIQUE KEY `uq_t_facilities` (`title`),
  KEY `fk_facilities_contexts` (`context_id`),
  KEY `fk_facilities_contact` (`contact_id`),
  KEY `ix_facilities_updated_at` (`updated_at`),
  KEY `fk_facilities_secondary_contact` (`secondary_contact_id`),
  CONSTRAINT `fk_facilities_contexts` FOREIGN KEY (`context_id`) REFERENCES `contexts` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `facilities`
--

LOCK TABLES `facilities` WRITE;
/*!40000 ALTER TABLE `facilities` DISABLE KEYS */;
/*!40000 ALTER TABLE `facilities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fulltext_record_properties`
--

DROP TABLE IF EXISTS `fulltext_record_properties`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fulltext_record_properties` (
  `key` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(64) NOT NULL,
  `tags` varchar(250) DEFAULT NULL,
  `property` varchar(64) NOT NULL,
  `content` text,
  `context_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`key`,`type`,`property`),
  KEY `ix_fulltext_record_properties_context_id` (`context_id`),
  KEY `ix_fulltext_record_properties_key` (`key`),
  KEY `ix_fulltext_record_properties_tags` (`tags`),
  KEY `ix_fulltext_record_properties_type` (`type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fulltext_record_properties`
--

LOCK TABLES `fulltext_record_properties` WRITE;
/*!40000 ALTER TABLE `fulltext_record_properties` DISABLE KEYS */;
/*!40000 ALTER TABLE `fulltext_record_properties` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ggrc_alembic_version`
--

DROP TABLE IF EXISTS `ggrc_alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ggrc_alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ggrc_alembic_version`
--

LOCK TABLES `ggrc_alembic_version` WRITE;
/*!40000 ALTER TABLE `ggrc_alembic_version` DISABLE KEYS */;
INSERT INTO `ggrc_alembic_version` VALUES ('297131e22e28');
/*!40000 ALTER TABLE `ggrc_alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `helps`
--

DROP TABLE IF EXISTS `helps`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `helps` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `modified_by_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `slug` varchar(250) NOT NULL,
  `title` varchar(250) NOT NULL,
  `content` text,
  `context_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_helps` (`slug`),
  KEY `fk_helps_contexts` (`context_id`),
  KEY `ix_helps_updated_at` (`updated_at`),
  CONSTRAINT `fk_helps_contexts` FOREIGN KEY (`context_id`) REFERENCES `contexts` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `helps`
--

LOCK TABLES `helps` WRITE;
/*!40000 ALTER TABLE `helps` DISABLE KEYS */;
/*!40000 ALTER TABLE `helps` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `issues`
--

DROP TABLE IF EXISTS `issues`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `issues` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `os_state` varchar(250) NOT NULL,
  `test_plan` text,
  `end_date` date DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `status` varchar(250) DEFAULT NULL,
  `notes` text,
  `description` text,
  `url` varchar(250) DEFAULT NULL,
  `reference_url` varchar(250) DEFAULT NULL,
  `secondary_contact_id` int(11) DEFAULT NULL,
  `contact_id` int(11) DEFAULT NULL,
  `title` varchar(250) NOT NULL,
  `slug` varchar(250) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `modified_by_id` int(11) DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `context_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_issues` (`slug`),
  UNIQUE KEY `uq_t_issues` (`title`),
  KEY `contact_id` (`contact_id`),
  KEY `context_id` (`context_id`),
  KEY `secondary_contact_id` (`secondary_contact_id`),
  CONSTRAINT `issues_ibfk_1` FOREIGN KEY (`contact_id`) REFERENCES `people` (`id`),
  CONSTRAINT `issues_ibfk_2` FOREIGN KEY (`context_id`) REFERENCES `contexts` (`id`),
  CONSTRAINT `issues_ibfk_3` FOREIGN KEY (`secondary_contact_id`) REFERENCES `people` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `issues`
--

LOCK TABLES `issues` WRITE;
/*!40000 ALTER TABLE `issues` DISABLE KEYS */;
/*!40000 ALTER TABLE `issues` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `markets`
--

DROP TABLE IF EXISTS `markets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `markets` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `modified_by_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `description` text,
  `url` varchar(250) DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `slug` varchar(250) NOT NULL,
  `title` varchar(250) NOT NULL,
  `context_id` int(11) DEFAULT NULL,
  `contact_id` int(11) DEFAULT NULL,
  `notes` text,
  `status` varchar(250) DEFAULT NULL,
  `reference_url` varchar(250) DEFAULT NULL,
  `secondary_contact_id` int(11) DEFAULT NULL,
  `os_state` varchar(16) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_markets` (`slug`),
  UNIQUE KEY `uq_t_markets` (`title`),
  KEY `fk_markets_contexts` (`context_id`),
  KEY `fk_markets_contact` (`contact_id`),
  KEY `ix_markets_updated_at` (`updated_at`),
  KEY `fk_markets_secondary_contact` (`secondary_contact_id`),
  CONSTRAINT `fk_markets_contexts` FOREIGN KEY (`context_id`) REFERENCES `contexts` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `markets`
--

LOCK TABLES `markets` WRITE;
/*!40000 ALTER TABLE `markets` DISABLE KEYS */;
/*!40000 ALTER TABLE `markets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `meetings`
--

DROP TABLE IF EXISTS `meetings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `meetings` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `response_id` int(11) NOT NULL,
  `title` varchar(250) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `modified_by_id` int(11) DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `context_id` int(11) DEFAULT NULL,
  `description` text,
  `start_at` datetime NOT NULL,
  `end_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `response_id` (`response_id`),
  KEY `fk_meetings_contexts` (`context_id`),
  KEY `ix_meetings_updated_at` (`updated_at`),
  CONSTRAINT `meetings_ibfk_1` FOREIGN KEY (`context_id`) REFERENCES `contexts` (`id`),
  CONSTRAINT `meetings_ibfk_3` FOREIGN KEY (`response_id`) REFERENCES `responses` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `meetings`
--

LOCK TABLES `meetings` WRITE;
/*!40000 ALTER TABLE `meetings` DISABLE KEYS */;
/*!40000 ALTER TABLE `meetings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notification_configs`
--

DROP TABLE IF EXISTS `notification_configs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `notification_configs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(250) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `modified_by_id` int(11) DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `context_id` int(11) DEFAULT NULL,
  `enable_flag` tinyint(1) DEFAULT NULL,
  `notif_type` varchar(250) DEFAULT NULL,
  `person_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_notif_configs_person_id_notif_type` (`person_id`,`notif_type`),
  KEY `fk_notification_configs_contexts` (`context_id`),
  KEY `ix_notification_configs_updated_at` (`updated_at`),
  CONSTRAINT `notification_configs_ibfk_1` FOREIGN KEY (`context_id`) REFERENCES `contexts` (`id`),
  CONSTRAINT `notification_configs_ibfk_2` FOREIGN KEY (`person_id`) REFERENCES `people` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notification_configs`
--

LOCK TABLES `notification_configs` WRITE;
/*!40000 ALTER TABLE `notification_configs` DISABLE KEYS */;
/*!40000 ALTER TABLE `notification_configs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notification_types`
--

DROP TABLE IF EXISTS `notification_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `notification_types` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(250) NOT NULL,
  `description` varchar(250) DEFAULT NULL,
  `advance_notice` int(11) DEFAULT NULL,
  `template` varchar(250) NOT NULL,
  `instant` tinyint(1) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `modified_by_id` int(11) DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `context_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `modified_by_id` (`modified_by_id`),
  CONSTRAINT `notification_types_ibfk_1` FOREIGN KEY (`modified_by_id`) REFERENCES `people` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notification_types`
--

LOCK TABLES `notification_types` WRITE;
/*!40000 ALTER TABLE `notification_types` DISABLE KEYS */;
/*!40000 ALTER TABLE `notification_types` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notifications`
--

DROP TABLE IF EXISTS `notifications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `notifications` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `object_id` int(11) NOT NULL,
  `object_type_id` int(11) NOT NULL,
  `notification_type_id` int(11) NOT NULL,
  `send_on` datetime NOT NULL,
  `sent_at` datetime DEFAULT NULL,
  `custom_message` text,
  `force_notifications` tinyint(1) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `modified_by_id` int(11) DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `context_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `object_type_id` (`object_type_id`),
  KEY `modified_by_id` (`modified_by_id`),
  KEY `fk_notification_type_id` (`notification_type_id`),
  CONSTRAINT `notifications_ibfk_1` FOREIGN KEY (`object_type_id`) REFERENCES `object_types` (`id`),
  CONSTRAINT `notifications_ibfk_2` FOREIGN KEY (`notification_type_id`) REFERENCES `notification_types` (`id`),
  CONSTRAINT `notifications_ibfk_3` FOREIGN KEY (`modified_by_id`) REFERENCES `people` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notifications`
--

LOCK TABLES `notifications` WRITE;
/*!40000 ALTER TABLE `notifications` DISABLE KEYS */;
/*!40000 ALTER TABLE `notifications` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `object_controls`
--

DROP TABLE IF EXISTS `object_controls`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `object_controls` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `modified_by_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `role` varchar(250) DEFAULT NULL,
  `notes` text,
  `control_id` int(11) NOT NULL,
  `controllable_id` int(11) NOT NULL,
  `controllable_type` varchar(250) NOT NULL,
  `context_id` int(11) DEFAULT NULL,
  `status` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_object_controls` (`control_id`,`controllable_id`,`controllable_type`),
  KEY `ix_control_id` (`control_id`),
  KEY `fk_object_controls_contexts` (`context_id`),
  KEY `ix_object_controls_updated_at` (`updated_at`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `object_controls`
--

LOCK TABLES `object_controls` WRITE;
/*!40000 ALTER TABLE `object_controls` DISABLE KEYS */;
/*!40000 ALTER TABLE `object_controls` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `object_documents`
--

DROP TABLE IF EXISTS `object_documents`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `object_documents` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `modified_by_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `role` varchar(250) DEFAULT NULL,
  `notes` text,
  `document_id` int(11) NOT NULL,
  `documentable_id` int(11) NOT NULL,
  `documentable_type` varchar(250) NOT NULL,
  `context_id` int(11) DEFAULT NULL,
  `status` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_object_documents` (`document_id`,`documentable_id`,`documentable_type`),
  KEY `fk_object_documents_contexts` (`context_id`),
  KEY `ix_document_id` (`document_id`),
  KEY `ix_object_documents_updated_at` (`updated_at`),
  CONSTRAINT `fk_object_documents_contexts` FOREIGN KEY (`context_id`) REFERENCES `contexts` (`id`),
  CONSTRAINT `object_documents_ibfk_1` FOREIGN KEY (`document_id`) REFERENCES `documents` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `object_documents`
--

LOCK TABLES `object_documents` WRITE;
/*!40000 ALTER TABLE `object_documents` DISABLE KEYS */;
/*!40000 ALTER TABLE `object_documents` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `object_objectives`
--

DROP TABLE IF EXISTS `object_objectives`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `object_objectives` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `modified_by_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `role` varchar(250) DEFAULT NULL,
  `notes` text,
  `objective_id` int(11) NOT NULL,
  `objectiveable_id` int(11) NOT NULL,
  `objectiveable_type` varchar(250) NOT NULL,
  `context_id` int(11) DEFAULT NULL,
  `status` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_object_objectives` (`objective_id`,`objectiveable_id`,`objectiveable_type`),
  KEY `ix_objective_id` (`objective_id`),
  KEY `fk_object_objectives_contexts` (`context_id`),
  KEY `ix_object_objectives_objectiveable` (`objectiveable_type`,`objectiveable_id`),
  KEY `ix_object_objectives_updated_at` (`updated_at`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `object_objectives`
--

LOCK TABLES `object_objectives` WRITE;
/*!40000 ALTER TABLE `object_objectives` DISABLE KEYS */;
/*!40000 ALTER TABLE `object_objectives` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `object_owners`
--

DROP TABLE IF EXISTS `object_owners`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `object_owners` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `person_id` int(11) NOT NULL,
  `ownable_id` int(11) NOT NULL,
  `ownable_type` varchar(250) NOT NULL,
  `modified_by_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `context_id` int(11) DEFAULT NULL,
  `status` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_id_owners` (`person_id`,`ownable_id`,`ownable_type`),
  KEY `fk_object_owners_contexts` (`context_id`),
  KEY `ix_object_owners_ownable` (`ownable_type`,`ownable_id`),
  KEY `ix_object_owners_updated_at` (`updated_at`),
  CONSTRAINT `object_owners_ibfk_1` FOREIGN KEY (`person_id`) REFERENCES `people` (`id`),
  CONSTRAINT `object_owners_ibfk_2` FOREIGN KEY (`context_id`) REFERENCES `contexts` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `object_owners`
--

LOCK TABLES `object_owners` WRITE;
/*!40000 ALTER TABLE `object_owners` DISABLE KEYS */;
/*!40000 ALTER TABLE `object_owners` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `object_people`
--

DROP TABLE IF EXISTS `object_people`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `object_people` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `modified_by_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `role` varchar(250) DEFAULT NULL,
  `notes` text,
  `person_id` int(11) NOT NULL,
  `personable_id` int(11) NOT NULL,
  `personable_type` varchar(250) NOT NULL,
  `context_id` int(11) DEFAULT NULL,
  `status` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_object_people` (`person_id`,`personable_id`,`personable_type`),
  KEY `fk_object_people_contexts` (`context_id`),
  KEY `ix_person_id` (`person_id`),
  KEY `ix_object_people_updated_at` (`updated_at`),
  CONSTRAINT `fk_object_people_contexts` FOREIGN KEY (`context_id`) REFERENCES `contexts` (`id`),
  CONSTRAINT `object_people_ibfk_1` FOREIGN KEY (`person_id`) REFERENCES `people` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `object_people`
--

LOCK TABLES `object_people` WRITE;
/*!40000 ALTER TABLE `object_people` DISABLE KEYS */;
/*!40000 ALTER TABLE `object_people` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `object_sections`
--

DROP TABLE IF EXISTS `object_sections`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `object_sections` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `modified_by_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `role` varchar(250) DEFAULT NULL,
  `notes` text,
  `section_id` int(11) NOT NULL,
  `sectionable_id` int(11) NOT NULL,
  `sectionable_type` varchar(250) NOT NULL,
  `context_id` int(11) DEFAULT NULL,
  `status` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_object_sections` (`section_id`,`sectionable_id`,`sectionable_type`),
  KEY `ix_section_id` (`section_id`),
  KEY `fk_object_sections_contexts` (`context_id`),
  KEY `ix_object_sections_updated_at` (`updated_at`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `object_sections`
--

LOCK TABLES `object_sections` WRITE;
/*!40000 ALTER TABLE `object_sections` DISABLE KEYS */;
/*!40000 ALTER TABLE `object_sections` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `object_types`
--

DROP TABLE IF EXISTS `object_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `object_types` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(250) NOT NULL,
  `description` varchar(250) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `modified_by_id` int(11) DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `context_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `object_types_name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `object_types`
--

LOCK TABLES `object_types` WRITE;
/*!40000 ALTER TABLE `object_types` DISABLE KEYS */;
/*!40000 ALTER TABLE `object_types` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `objective_controls`
--

DROP TABLE IF EXISTS `objective_controls`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `objective_controls` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `modified_by_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `objective_id` int(11) NOT NULL,
  `control_id` int(11) NOT NULL,
  `context_id` int(11) DEFAULT NULL,
  `status` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_objective_controls` (`objective_id`,`control_id`),
  KEY `ix_objective_id` (`objective_id`),
  KEY `ix_control_id` (`control_id`),
  KEY `fk_objective_controls_contexts` (`context_id`),
  KEY `ix_objective_controls_updated_at` (`updated_at`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `objective_controls`
--

LOCK TABLES `objective_controls` WRITE;
/*!40000 ALTER TABLE `objective_controls` DISABLE KEYS */;
/*!40000 ALTER TABLE `objective_controls` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `objectives`
--

DROP TABLE IF EXISTS `objectives`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `objectives` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `modified_by_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `description` text,
  `url` varchar(250) DEFAULT NULL,
  `slug` varchar(250) NOT NULL,
  `title` varchar(250) NOT NULL,
  `notes` text,
  `context_id` int(11) DEFAULT NULL,
  `contact_id` int(11) DEFAULT NULL,
  `status` varchar(250) DEFAULT NULL,
  `reference_url` varchar(250) DEFAULT NULL,
  `secondary_contact_id` int(11) DEFAULT NULL,
  `os_state` varchar(16) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_objectives` (`slug`),
  UNIQUE KEY `uq_t_objectives` (`title`),
  KEY `fk_objectives_contact` (`contact_id`),
  KEY `fk_objectives_contexts` (`context_id`),
  KEY `ix_objectives_updated_at` (`updated_at`),
  KEY `fk_objectives_secondary_contact` (`secondary_contact_id`),
  CONSTRAINT `objectives_ibfk_1` FOREIGN KEY (`context_id`) REFERENCES `contexts` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `objectives`
--

LOCK TABLES `objectives` WRITE;
/*!40000 ALTER TABLE `objectives` DISABLE KEYS */;
/*!40000 ALTER TABLE `objectives` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `options`
--

DROP TABLE IF EXISTS `options`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `options` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `modified_by_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `description` text,
  `role` varchar(250) DEFAULT NULL,
  `title` varchar(250) DEFAULT NULL,
  `required` tinyint(1) DEFAULT NULL,
  `context_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_options_contexts` (`context_id`),
  KEY `ix_options_role` (`role`),
  KEY `ix_options_updated_at` (`updated_at`),
  CONSTRAINT `fk_options_contexts` FOREIGN KEY (`context_id`) REFERENCES `contexts` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=142 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `options`
--

LOCK TABLES `options` WRITE;
/*!40000 ALTER TABLE `options` DISABLE KEYS */;
INSERT INTO `options` VALUES (1,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'asset_type','Client List',NULL,NULL),(2,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'asset_type','Employee List',NULL,NULL),(3,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'asset_type','Ledger Accounts',NULL,NULL),(4,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'asset_type','Patents',NULL,NULL),(5,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'asset_type','Personal Identifiable Info',NULL,NULL),(6,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'asset_type','Source Code',NULL,NULL),(7,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'asset_type','User Data',NULL,NULL),(8,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'audit_duration','1 Month',NULL,NULL),(9,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'audit_duration','1 Week',NULL,NULL),(10,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'audit_duration','1 Year',NULL,NULL),(11,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'audit_duration','2 Months',NULL,NULL),(12,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'audit_duration','2 Weeks',NULL,NULL),(13,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'audit_duration','3 Months',NULL,NULL),(14,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'audit_duration','4 Months',NULL,NULL),(15,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'audit_duration','6 Months',NULL,NULL),(16,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'audit_frequency','Ad-Hoc',NULL,NULL),(17,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'audit_frequency','Annual',NULL,NULL),(18,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'audit_frequency','Bi-Annual',NULL,NULL),(19,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'audit_frequency','Continuous',NULL,NULL),(20,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'audit_frequency','Daily',NULL,NULL),(21,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'audit_frequency','Hourly',NULL,NULL),(22,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'audit_frequency','Monthly',NULL,NULL),(23,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'audit_frequency','Quarterly',NULL,NULL),(24,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'audit_frequency','Semi-Annual',NULL,NULL),(25,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'audit_frequency','Weekly',NULL,NULL),(27,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'control_kind','Detective',NULL,NULL),(28,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'control_kind','Preventative',NULL,NULL),(38,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'directive_kind','Company Policy',NULL,NULL),(39,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'directive_kind','Data Asset Policy',NULL,NULL),(40,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'directive_kind','Operational Group Policy',NULL,NULL),(41,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'directive_kind','Regulation',NULL,NULL),(42,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'document_status','active',NULL,NULL),(43,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'document_status','deprecated',NULL,NULL),(44,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'document_type','Excel',NULL,NULL),(45,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'document_type','PDF',NULL,NULL),(46,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'document_type','Text',NULL,NULL),(47,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'document_type','URL',NULL,NULL),(48,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'document_type','Word',NULL,NULL),(49,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'document_year','1980',NULL,NULL),(50,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'document_year','1981',NULL,NULL),(51,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'document_year','1982',NULL,NULL),(52,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'document_year','1983',NULL,NULL),(53,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'document_year','1984',NULL,NULL),(54,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'document_year','1985',NULL,NULL),(55,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'document_year','1986',NULL,NULL),(56,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'document_year','1987',NULL,NULL),(57,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'document_year','1988',NULL,NULL),(58,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'document_year','1989',NULL,NULL),(59,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'document_year','1990',NULL,NULL),(60,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'document_year','1991',NULL,NULL),(61,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'document_year','1992',NULL,NULL),(62,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'document_year','1993',NULL,NULL),(63,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'document_year','1994',NULL,NULL),(64,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'document_year','1995',NULL,NULL),(65,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'document_year','1996',NULL,NULL),(66,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'document_year','1997',NULL,NULL),(67,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'document_year','1998',NULL,NULL),(68,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'document_year','1999',NULL,NULL),(69,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'document_year','2000',NULL,NULL),(70,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'document_year','2001',NULL,NULL),(71,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'document_year','2002',NULL,NULL),(72,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'document_year','2003',NULL,NULL),(73,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'document_year','2004',NULL,NULL),(74,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'document_year','2005',NULL,NULL),(75,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'document_year','2006',NULL,NULL),(76,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'document_year','2007',NULL,NULL),(77,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'document_year','2008',NULL,NULL),(78,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'document_year','2009',NULL,NULL),(79,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'document_year','2010',NULL,NULL),(80,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'document_year','2011',NULL,NULL),(81,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'document_year','2012',NULL,NULL),(82,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'document_year','2013',0,NULL),(83,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'entity_kind','Not Applicable',NULL,NULL),(84,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'entity_type','Business Unit',NULL,NULL),(85,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'entity_type','Division',NULL,NULL),(86,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'entity_type','Functional Group',NULL,NULL),(87,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'entity_type','Legal Entity',NULL,NULL),(88,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'language','English',NULL,NULL),(89,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'location_kind','Building',NULL,NULL),(90,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'location_kind','HazMat Storage',NULL,NULL),(91,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'location_kind','Kitchen',NULL,NULL),(92,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'location_kind','Lab',NULL,NULL),(93,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'location_kind','Machine Room',NULL,NULL),(94,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'location_kind','Maintenance Facility',NULL,NULL),(95,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'location_kind','Office',NULL,NULL),(96,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'location_kind','Parking Garage',NULL,NULL),(97,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'location_kind','Workshop',NULL,NULL),(98,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'location_type','Colo Data Center',NULL,NULL),(99,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'location_type','Contract Manufacturer',NULL,NULL),(100,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'location_type','Data Center',NULL,NULL),(101,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'location_type','Distribution Center',NULL,NULL),(102,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'location_type','Headquarters',NULL,NULL),(103,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'location_type','Regional Office',NULL,NULL),(104,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'location_type','Sales Office',NULL,NULL),(105,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'location_type','Vendor Worksite',NULL,NULL),(106,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'network_zone','Corp',0,NULL),(107,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'network_zone','Prod',0,NULL),(108,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'person_language','English',NULL,NULL),(109,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'product_kind','Not Applicable',NULL,NULL),(110,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'product_type','Appliance',NULL,NULL),(111,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'product_type','Desktop Software',NULL,NULL),(112,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'product_type','SaaS',NULL,NULL),(113,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'reference_type','Database',NULL,NULL),(114,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'reference_type','Document',NULL,NULL),(115,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'reference_type','Numeric Data',NULL,NULL),(116,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'reference_type','Screenshot',NULL,NULL),(117,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'reference_type','Simple Text',NULL,NULL),(118,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'reference_type','Website',NULL,NULL),(119,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'system_kind','Infrastructure',NULL,NULL),(120,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'system_type','Infrastructure',NULL,NULL),(121,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'threat_type','Insider Threat',NULL,NULL),(122,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'threat_type','Outsider Threat',NULL,NULL),(123,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'verify_frequency','Bi-Weekly',NULL,NULL),(124,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'verify_frequency','Yearly',NULL,NULL),(125,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'verify_frequency','Bi-Monthly',NULL,NULL),(126,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'verify_frequency','Continuous',NULL,NULL),(127,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'verify_frequency','Daily',NULL,NULL),(128,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'verify_frequency','Hourly',NULL,NULL),(129,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'verify_frequency','Indeterminate',0,NULL),(130,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'verify_frequency','Monthly',NULL,NULL),(131,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'verify_frequency','Quarterly',NULL,NULL),(132,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'verify_frequency','Semi-Annually',NULL,NULL),(133,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'verify_frequency','Transactional',0,NULL),(134,NULL,'2016-05-03 10:37:02','2016-05-03 10:37:02',NULL,'verify_frequency','Weekly',NULL,NULL),(135,NULL,NULL,NULL,NULL,'network_zone','3rd Party',NULL,NULL),(136,NULL,NULL,NULL,NULL,'network_zone','Core',NULL,NULL),(137,NULL,NULL,NULL,NULL,'network_zone','Service',NULL,NULL),(138,NULL,NULL,NULL,NULL,'control_kind','Corrective',NULL,NULL),(139,NULL,NULL,NULL,NULL,'control_means','Technical',NULL,NULL),(140,NULL,NULL,NULL,NULL,'control_means','Administrative',NULL,NULL),(141,NULL,NULL,NULL,NULL,'control_means','Physical',NULL,NULL);
/*!40000 ALTER TABLE `options` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `org_groups`
--

DROP TABLE IF EXISTS `org_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `org_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `modified_by_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `description` text,
  `url` varchar(250) DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `slug` varchar(250) NOT NULL,
  `title` varchar(250) NOT NULL,
  `context_id` int(11) DEFAULT NULL,
  `contact_id` int(11) DEFAULT NULL,
  `notes` text,
  `status` varchar(250) DEFAULT NULL,
  `reference_url` varchar(250) DEFAULT NULL,
  `secondary_contact_id` int(11) DEFAULT NULL,
  `os_state` varchar(16) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_org_groups` (`slug`),
  UNIQUE KEY `uq_t_org_groups` (`title`),
  KEY `fk_org_groups_contexts` (`context_id`),
  KEY `fk_org_groups_contact` (`contact_id`),
  KEY `ix_org_groups_updated_at` (`updated_at`),
  KEY `fk_org_groups_secondary_contact` (`secondary_contact_id`),
  CONSTRAINT `fk_org_groups_contexts` FOREIGN KEY (`context_id`) REFERENCES `contexts` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `org_groups`
--

LOCK TABLES `org_groups` WRITE;
/*!40000 ALTER TABLE `org_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `org_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `people`
--

DROP TABLE IF EXISTS `people`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `people` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `modified_by_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `email` varchar(250) NOT NULL,
  `name` varchar(250) DEFAULT NULL,
  `language_id` int(11) DEFAULT NULL,
  `company` varchar(250) DEFAULT NULL,
  `context_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_people_email` (`email`),
  KEY `fk_people_contexts` (`context_id`),
  KEY `ix_people_name_email` (`name`,`email`),
  KEY `ix_people_updated_at` (`updated_at`),
  CONSTRAINT `fk_people_contexts` FOREIGN KEY (`context_id`) REFERENCES `contexts` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `people`
--

LOCK TABLES `people` WRITE;
/*!40000 ALTER TABLE `people` DISABLE KEYS */;
/*!40000 ALTER TABLE `people` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `modified_by_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `description` text,
  `url` varchar(250) DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `slug` varchar(250) NOT NULL,
  `title` varchar(250) NOT NULL,
  `kind_id` int(11) DEFAULT NULL,
  `version` varchar(250) DEFAULT NULL,
  `context_id` int(11) DEFAULT NULL,
  `contact_id` int(11) DEFAULT NULL,
  `notes` text,
  `status` varchar(250) DEFAULT NULL,
  `reference_url` varchar(250) DEFAULT NULL,
  `secondary_contact_id` int(11) DEFAULT NULL,
  `os_state` varchar(16) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_products` (`slug`),
  UNIQUE KEY `uq_t_products` (`title`),
  KEY `fk_products_contexts` (`context_id`),
  KEY `fk_products_contact` (`contact_id`),
  KEY `ix_products_updated_at` (`updated_at`),
  KEY `fk_products_secondary_contact` (`secondary_contact_id`),
  CONSTRAINT `fk_products_contexts` FOREIGN KEY (`context_id`) REFERENCES `contexts` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `program_controls`
--

DROP TABLE IF EXISTS `program_controls`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `program_controls` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `modified_by_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `context_id` int(11) DEFAULT NULL,
  `program_id` int(11) NOT NULL,
  `control_id` int(11) NOT NULL,
  `status` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_program_controls` (`program_id`,`control_id`),
  KEY `ix_program_id` (`program_id`),
  KEY `ix_control_id` (`control_id`),
  KEY `fk_program_controls_contexts` (`context_id`),
  KEY `ix_program_controls_updated_at` (`updated_at`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `program_controls`
--

LOCK TABLES `program_controls` WRITE;
/*!40000 ALTER TABLE `program_controls` DISABLE KEYS */;
/*!40000 ALTER TABLE `program_controls` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `program_directives`
--

DROP TABLE IF EXISTS `program_directives`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `program_directives` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `modified_by_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `program_id` int(11) NOT NULL,
  `directive_id` int(11) NOT NULL,
  `context_id` int(11) DEFAULT NULL,
  `status` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_program_directives` (`program_id`,`directive_id`),
  KEY `fk_program_directives_contexts` (`context_id`),
  KEY `ix_directive_id` (`directive_id`),
  KEY `ix_program_id` (`program_id`),
  KEY `ix_program_directives_updated_at` (`updated_at`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `program_directives`
--

LOCK TABLES `program_directives` WRITE;
/*!40000 ALTER TABLE `program_directives` DISABLE KEYS */;
/*!40000 ALTER TABLE `program_directives` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `programs`
--

DROP TABLE IF EXISTS `programs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `programs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `modified_by_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `description` text,
  `url` varchar(250) DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `slug` varchar(250) NOT NULL,
  `title` varchar(250) NOT NULL,
  `kind` varchar(250) DEFAULT NULL,
  `context_id` int(11) DEFAULT NULL,
  `contact_id` int(11) DEFAULT NULL,
  `notes` text,
  `status` varchar(250) DEFAULT NULL,
  `reference_url` varchar(250) DEFAULT NULL,
  `private` tinyint(1) NOT NULL,
  `secondary_contact_id` int(11) DEFAULT NULL,
  `os_state` varchar(16) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_programs` (`slug`),
  UNIQUE KEY `uq_t_programs` (`title`),
  KEY `fk_programs_contexts` (`context_id`),
  KEY `fk_programs_contact` (`contact_id`),
  KEY `ix_programs_updated_at` (`updated_at`),
  KEY `fk_programs_secondary_contact` (`secondary_contact_id`),
  CONSTRAINT `fk_programs_contexts` FOREIGN KEY (`context_id`) REFERENCES `contexts` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `programs`
--

LOCK TABLES `programs` WRITE;
/*!40000 ALTER TABLE `programs` DISABLE KEYS */;
/*!40000 ALTER TABLE `programs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects`
--

DROP TABLE IF EXISTS `projects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `projects` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `modified_by_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `description` text,
  `url` varchar(250) DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `slug` varchar(250) NOT NULL,
  `title` varchar(250) NOT NULL,
  `context_id` int(11) DEFAULT NULL,
  `contact_id` int(11) DEFAULT NULL,
  `notes` text,
  `status` varchar(250) DEFAULT NULL,
  `reference_url` varchar(250) DEFAULT NULL,
  `secondary_contact_id` int(11) DEFAULT NULL,
  `os_state` varchar(16) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_projects` (`slug`),
  UNIQUE KEY `uq_t_projects` (`title`),
  KEY `fk_projects_contexts` (`context_id`),
  KEY `fk_projects_contact` (`contact_id`),
  KEY `ix_projects_updated_at` (`updated_at`),
  KEY `fk_projects_secondary_contact` (`secondary_contact_id`),
  CONSTRAINT `fk_projects_contexts` FOREIGN KEY (`context_id`) REFERENCES `contexts` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects`
--

LOCK TABLES `projects` WRITE;
/*!40000 ALTER TABLE `projects` DISABLE KEYS */;
/*!40000 ALTER TABLE `projects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `relationship_attrs`
--

DROP TABLE IF EXISTS `relationship_attrs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `relationship_attrs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `relationship_id` int(11) NOT NULL,
  `attr_name` varchar(250) NOT NULL,
  `attr_value` varchar(250) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `relationship_id` (`relationship_id`),
  CONSTRAINT `relationship_attrs_ibfk_1` FOREIGN KEY (`relationship_id`) REFERENCES `relationships` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `relationship_attrs`
--

LOCK TABLES `relationship_attrs` WRITE;
/*!40000 ALTER TABLE `relationship_attrs` DISABLE KEYS */;
/*!40000 ALTER TABLE `relationship_attrs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `relationship_types`
--

DROP TABLE IF EXISTS `relationship_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `relationship_types` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `modified_by_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `description` text,
  `relationship_type` varchar(250) DEFAULT NULL,
  `forward_phrase` varchar(250) DEFAULT NULL,
  `backward_phrase` varchar(250) DEFAULT NULL,
  `symmetric` tinyint(1) NOT NULL,
  `context_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_relationship_types_contexts` (`context_id`),
  KEY `ix_relationship_types_updated_at` (`updated_at`),
  CONSTRAINT `fk_relationship_types_contexts` FOREIGN KEY (`context_id`) REFERENCES `contexts` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `relationship_types`
--

LOCK TABLES `relationship_types` WRITE;
/*!40000 ALTER TABLE `relationship_types` DISABLE KEYS */;
/*!40000 ALTER TABLE `relationship_types` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `relationships`
--

DROP TABLE IF EXISTS `relationships`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `relationships` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `modified_by_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `source_id` int(11) NOT NULL,
  `source_type` varchar(250) NOT NULL,
  `destination_id` int(11) NOT NULL,
  `destination_type` varchar(250) NOT NULL,
  `relationship_type_id` varchar(250) DEFAULT NULL,
  `context_id` int(11) DEFAULT NULL,
  `status` varchar(250) DEFAULT NULL,
  `automapping_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_relationships` (`source_id`,`source_type`,`destination_id`,`destination_type`),
  KEY `fk_relationships_contexts` (`context_id`),
  KEY `ix_relationships_destination` (`destination_type`,`destination_id`),
  KEY `ix_relationships_source` (`source_type`,`source_id`),
  KEY `ix_relationships_updated_at` (`updated_at`),
  KEY `relationships_automapping_parent` (`automapping_id`),
  CONSTRAINT `relationships_automapping_parent` FOREIGN KEY (`automapping_id`) REFERENCES `relationships` (`id`) ON DELETE SET NULL,
  CONSTRAINT `fk_relationships_contexts` FOREIGN KEY (`context_id`) REFERENCES `contexts` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `relationships`
--

LOCK TABLES `relationships` WRITE;
/*!40000 ALTER TABLE `relationships` DISABLE KEYS */;
/*!40000 ALTER TABLE `relationships` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `requests`
--

DROP TABLE IF EXISTS `requests`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `requests` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `assignee_id` int(11) DEFAULT NULL,
  `request_type` enum('documentation','interview','population sample') NOT NULL,
  `status` enum('Open','In Progress','Finished','Verified','Final') NOT NULL,
  `requested_on` date NOT NULL,
  `due_on` date NOT NULL,
  `audit_id` int(11) NOT NULL,
  `gdrive_upload_path` varchar(250) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `modified_by_id` int(11) DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `context_id` int(11) DEFAULT NULL,
  `test` text,
  `notes` text,
  `description` text,
  `requestor_id` int(11) DEFAULT NULL,
  `slug` varchar(250) NOT NULL,
  `title` varchar(250) DEFAULT NULL,
  `audit_object_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_requests` (`slug`),
  KEY `audit_id` (`audit_id`),
  KEY `fk_requests_contexts` (`context_id`),
  KEY `ix_requests_updated_at` (`updated_at`),
  KEY `requests_audit_objects_ibfk` (`audit_object_id`),
  CONSTRAINT `requests_audit_objects_ibfk` FOREIGN KEY (`audit_object_id`) REFERENCES `audit_objects` (`id`),
  CONSTRAINT `requests_ibfk_2` FOREIGN KEY (`audit_id`) REFERENCES `audits` (`id`),
  CONSTRAINT `requests_ibfk_3` FOREIGN KEY (`context_id`) REFERENCES `contexts` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `requests`
--

LOCK TABLES `requests` WRITE;
/*!40000 ALTER TABLE `requests` DISABLE KEYS */;
/*!40000 ALTER TABLE `requests` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `responses`
--

DROP TABLE IF EXISTS `responses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `responses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `request_id` int(11) NOT NULL,
  `response_type` enum('documentation','interview','population sample') NOT NULL,
  `status` varchar(250) NOT NULL,
  `contact_id` int(11) DEFAULT NULL,
  `title` varchar(250) NOT NULL,
  `slug` varchar(250) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `modified_by_id` int(11) DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `context_id` int(11) DEFAULT NULL,
  `description` text,
  `url` varchar(250) DEFAULT NULL,
  `population_count` int(11) DEFAULT NULL,
  `sample_count` int(11) DEFAULT NULL,
  `population_worksheet_id` int(11) DEFAULT NULL,
  `sample_worksheet_id` int(11) DEFAULT NULL,
  `sample_evidence_id` int(11) DEFAULT NULL,
  `notes` text,
  `reference_url` varchar(250) DEFAULT NULL,
  `secondary_contact_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `request_id` (`request_id`),
  KEY `population_worksheet_document` (`population_worksheet_id`),
  KEY `sample_worksheet_document` (`sample_worksheet_id`),
  KEY `sample_evidence_document` (`sample_evidence_id`),
  KEY `fk_responses_contact` (`contact_id`),
  KEY `fk_responses_contexts` (`context_id`),
  KEY `ix_responses_updated_at` (`updated_at`),
  KEY `fk_responses_secondary_contact` (`secondary_contact_id`),
  CONSTRAINT `population_worksheet_document` FOREIGN KEY (`population_worksheet_id`) REFERENCES `documents` (`id`),
  CONSTRAINT `responses_ibfk_1` FOREIGN KEY (`context_id`) REFERENCES `contexts` (`id`),
  CONSTRAINT `responses_ibfk_3` FOREIGN KEY (`request_id`) REFERENCES `requests` (`id`),
  CONSTRAINT `sample_evidence_document` FOREIGN KEY (`sample_evidence_id`) REFERENCES `documents` (`id`),
  CONSTRAINT `sample_worksheet_document` FOREIGN KEY (`sample_worksheet_id`) REFERENCES `documents` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `responses`
--

LOCK TABLES `responses` WRITE;
/*!40000 ALTER TABLE `responses` DISABLE KEYS */;
/*!40000 ALTER TABLE `responses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `revisions`
--

DROP TABLE IF EXISTS `revisions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `revisions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `resource_id` int(11) NOT NULL,
  `resource_type` varchar(250) NOT NULL,
  `event_id` int(11) NOT NULL,
  `action` enum('created','modified','deleted') NOT NULL,
  `content` text NOT NULL,
  `context_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `modified_by_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `event_id` (`event_id`),
  KEY `revisions_modified_by` (`modified_by_id`),
  KEY `fk_revisions_contexts` (`context_id`),
  KEY `ix_revisions_updated_at` (`updated_at`),
  CONSTRAINT `fk_revisions_contexts` FOREIGN KEY (`context_id`) REFERENCES `contexts` (`id`),
  CONSTRAINT `revisions_ibfk_1` FOREIGN KEY (`event_id`) REFERENCES `events` (`id`),
  CONSTRAINT `revisions_modified_by` FOREIGN KEY (`modified_by_id`) REFERENCES `people` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `revisions`
--

LOCK TABLES `revisions` WRITE;
/*!40000 ALTER TABLE `revisions` DISABLE KEYS */;
/*!40000 ALTER TABLE `revisions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `section_objectives`
--

DROP TABLE IF EXISTS `section_objectives`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `section_objectives` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `modified_by_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `section_id` int(11) NOT NULL,
  `objective_id` int(11) NOT NULL,
  `context_id` int(11) DEFAULT NULL,
  `status` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_section_objectives` (`section_id`,`objective_id`),
  KEY `ix_section_id` (`section_id`),
  KEY `ix_objective_id` (`objective_id`),
  KEY `fk_section_objectives_contexts` (`context_id`),
  KEY `ix_section_objectives_updated_at` (`updated_at`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `section_objectives`
--

LOCK TABLES `section_objectives` WRITE;
/*!40000 ALTER TABLE `section_objectives` DISABLE KEYS */;
/*!40000 ALTER TABLE `section_objectives` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sections`
--

DROP TABLE IF EXISTS `sections`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sections` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `modified_by_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `description` text,
  `url` varchar(250) DEFAULT NULL,
  `slug` varchar(250) NOT NULL,
  `title` varchar(250) NOT NULL,
  `na` tinyint(1) NOT NULL,
  `notes` text,
  `parent_id` int(11) DEFAULT NULL,
  `context_id` int(11) DEFAULT NULL,
  `contact_id` int(11) DEFAULT NULL,
  `reference_url` varchar(250) DEFAULT NULL,
  `secondary_contact_id` int(11) DEFAULT NULL,
  `os_state` varchar(16) NOT NULL,
  `status` varchar(250) DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_sections` (`slug`),
  UNIQUE KEY `uq_t_sections` (`title`),
  KEY `parent_id` (`parent_id`),
  KEY `fk_sections_contexts` (`context_id`),
  KEY `fk_sections_contact` (`contact_id`),
  KEY `ix_sections_updated_at` (`updated_at`),
  KEY `fk_sections_secondary_contact` (`secondary_contact_id`),
  CONSTRAINT `fk_sections_contexts` FOREIGN KEY (`context_id`) REFERENCES `contexts` (`id`),
  CONSTRAINT `sections_ibfk_2` FOREIGN KEY (`parent_id`) REFERENCES `sections` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sections`
--

LOCK TABLES `sections` WRITE;
/*!40000 ALTER TABLE `sections` DISABLE KEYS */;
/*!40000 ALTER TABLE `sections` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `systems`
--

DROP TABLE IF EXISTS `systems`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `systems` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `modified_by_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `description` text,
  `url` varchar(250) DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `slug` varchar(250) NOT NULL,
  `title` varchar(250) NOT NULL,
  `infrastructure` tinyint(1) DEFAULT NULL,
  `contact_id` int(11) DEFAULT NULL,
  `is_biz_process` tinyint(1) DEFAULT NULL,
  `version` varchar(250) DEFAULT NULL,
  `notes` text,
  `network_zone_id` int(11) DEFAULT NULL,
  `context_id` int(11) DEFAULT NULL,
  `status` varchar(250) DEFAULT NULL,
  `reference_url` varchar(250) DEFAULT NULL,
  `secondary_contact_id` int(11) DEFAULT NULL,
  `os_state` varchar(16) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_systems` (`slug`),
  UNIQUE KEY `uq_t_systems` (`title`),
  KEY `fk_systems_contexts` (`context_id`),
  KEY `fk_systems_contact` (`contact_id`),
  KEY `ix_systems_is_biz_process` (`is_biz_process`),
  KEY `ix_systems_updated_at` (`updated_at`),
  KEY `fk_systems_secondary_contact` (`secondary_contact_id`),
  CONSTRAINT `fk_systems_contexts` FOREIGN KEY (`context_id`) REFERENCES `contexts` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `systems`
--

LOCK TABLES `systems` WRITE;
/*!40000 ALTER TABLE `systems` DISABLE KEYS */;
/*!40000 ALTER TABLE `systems` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vendors`
--

DROP TABLE IF EXISTS `vendors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vendors` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `modified_by_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `description` text,
  `url` varchar(250) DEFAULT NULL,
  `start_date` datetime DEFAULT NULL,
  `end_date` datetime DEFAULT NULL,
  `slug` varchar(250) NOT NULL,
  `title` varchar(250) NOT NULL,
  `context_id` int(11) DEFAULT NULL,
  `contact_id` int(11) DEFAULT NULL,
  `notes` text,
  `status` varchar(250) NOT NULL,
  `reference_url` varchar(250) DEFAULT NULL,
  `secondary_contact_id` int(11) DEFAULT NULL,
  `os_state` varchar(16) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_vendors_title` (`title`),
  UNIQUE KEY `uq_slug_vendors` (`slug`),
  KEY `fk_vendors_context` (`context_id`),
  KEY `fk_vendors_contact` (`contact_id`),
  KEY `fk_vendors_modified_by` (`modified_by_id`),
  KEY `fk_vendors_status` (`status`),
  KEY `ix_vendors_updated_at` (`updated_at`),
  KEY `fk_vendors_secondary_contact` (`secondary_contact_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vendors`
--

LOCK TABLES `vendors` WRITE;
/*!40000 ALTER TABLE `vendors` DISABLE KEYS */;
/*!40000 ALTER TABLE `vendors` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-05-03 10:39:38
