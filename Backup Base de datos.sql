-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 21-01-2022 a las 06:28:29
-- Versión del servidor: 8.0.17
-- Versión de PHP: 7.3.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bodega`
--
CREATE DATABASE IF NOT EXISTS `bodega` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `bodega`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add bodega', 7, 'add_bodega'),
(26, 'Can change bodega', 7, 'change_bodega'),
(27, 'Can delete bodega', 7, 'delete_bodega'),
(28, 'Can view bodega', 7, 'view_bodega'),
(29, 'Can add producto', 8, 'add_producto'),
(30, 'Can change producto', 8, 'change_producto'),
(31, 'Can delete producto', 8, 'delete_producto'),
(32, 'Can view producto', 8, 'view_producto'),
(33, 'Can add usuario', 9, 'add_usuario'),
(34, 'Can change usuario', 9, 'change_usuario'),
(35, 'Can delete usuario', 9, 'delete_usuario'),
(36, 'Can view usuario', 9, 'view_usuario'),
(37, 'Can add bodega producto', 10, 'add_bodegaproducto'),
(38, 'Can change bodega producto', 10, 'change_bodegaproducto'),
(39, 'Can delete bodega producto', 10, 'delete_bodegaproducto'),
(40, 'Can view bodega producto', 10, 'view_bodegaproducto');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$260000$S5ek4d9Jys1mE4Vj2JwcGS$SYlG0KVAIJem/tSf9WXKVSUuItDYDDmFc2Ew582T50s=', '2022-01-21 05:58:06.633333', 1, 'admin', '', '', 'msalinasnicoletti@gmail.com', 1, 1, '2022-01-21 05:58:04.578136');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `bodega_bodega`
--

CREATE TABLE `bodega_bodega` (
  `id` int(11) NOT NULL,
  `nombre` varchar(70) NOT NULL,
  `direccion` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `bodega_bodega`
--

INSERT INTO `bodega_bodega` (`id`, `nombre`, `direccion`) VALUES
(1, 'Bodega Santiago Centro', 'Moneda 665'),
(2, 'Bodega Providencia', 'Hernando de Aguirre 162');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `bodega_bodegaproducto`
--

CREATE TABLE `bodega_bodegaproducto` (
  `id` int(11) NOT NULL,
  `stock` int(11) NOT NULL,
  `idBodega_id` int(11) NOT NULL,
  `idProducto_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `bodega_bodegaproducto`
--

INSERT INTO `bodega_bodegaproducto` (`id`, `stock`, `idBodega_id`, `idProducto_id`) VALUES
(1, 15, 1, 1),
(2, 8, 1, 4),
(3, 7, 1, 7),
(4, 3, 1, 8),
(5, 8, 2, 4),
(6, 4, 2, 6),
(7, 12, 2, 8),
(8, 2, 2, 3),
(9, 3, 1, 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `bodega_producto`
--

CREATE TABLE `bodega_producto` (
  `id` int(11) NOT NULL,
  `codigo` varchar(50) NOT NULL,
  `nombre` varchar(70) NOT NULL,
  `detalle` longtext NOT NULL,
  `valor` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `bodega_producto`
--

INSERT INTO `bodega_producto` (`id`, `codigo`, `nombre`, `detalle`, `valor`) VALUES
(1, 'AF01', 'Xiaomi Poco x3 PRO', 'smartphone xiaomi poco x3 pro\n6GB ram 128GB rom', 220000),
(2, 'AX90', 'Samsung Glaxy Note10+', '12GB RAM 256GB ROM', 400000),
(3, 'MI20K', 'Redmi K20 Pro', '6GB RAM 64GB ROM', 125000),
(4, 'PL6541', 'Realme X2 Pro', '6GB RAM 64GB ROM', 135000),
(5, 'ZD654', 'OnePlus 8T', '8GB RAM 128GB ROM', 180000),
(6, 'MOT652', 'Motorola Moto G8', '4GB RAM 64GB ROM', 155000),
(7, 'HU956', 'Huawei P20', '4GB RAM 128ROM', 165000),
(8, 'YP652', 'HTC U Ultra', '4GB RAM 64GB RAM', 120000);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `bodega_usuario`
--

CREATE TABLE `bodega_usuario` (
  `id` int(11) NOT NULL,
  `email` varchar(254) NOT NULL,
  `password` varchar(50) NOT NULL,
  `nombres` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `bodega_usuario`
--

INSERT INTO `bodega_usuario` (`id`, `email`, `password`, `nombres`) VALUES
(1, 'admin@admin.cl', 'sha1$$d033e22ae348aeb5660fc2140aec35850c4da997', 'Miguel Salinas');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ;

--
-- Volcado de datos para la tabla `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2022-01-21 05:58:36.382954', '1', 'usuario object (1)', 1, '[{\"added\": {}}]', 9, 1),
(2, '2022-01-21 05:59:11.016275', '1', 'usuario object (1)', 2, '[{\"changed\": {\"fields\": [\"Password\"]}}]', 9, 1),
(3, '2022-01-21 06:00:19.431091', '1', 'usuario object (1)', 2, '[{\"changed\": {\"fields\": [\"Password\"]}}]', 9, 1),
(4, '2022-01-21 06:14:03.761801', '2', 'usuario object (2)', 1, '[{\"added\": {}}]', 9, 1),
(5, '2022-01-21 06:15:58.513995', '3', 'usuario object (3)', 1, '[{\"added\": {}}]', 9, 1),
(6, '2022-01-21 06:22:15.267912', '3', 'usuario object (3)', 2, '[{\"changed\": {\"fields\": [\"Password\"]}}]', 9, 1),
(7, '2022-01-21 06:22:31.507902', '3', 'usuario object (3)', 3, '', 9, 1),
(8, '2022-01-21 06:22:31.509821', '2', 'usuario object (2)', 3, '', 9, 1),
(9, '2022-01-21 06:22:37.155452', '1', 'usuario object (1)', 2, '[{\"changed\": {\"fields\": [\"Password\"]}}]', 9, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(7, 'bodega', 'bodega'),
(10, 'bodega', 'bodegaproducto'),
(8, 'bodega', 'producto'),
(9, 'bodega', 'usuario'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-01-21 05:57:10.507891'),
(2, 'auth', '0001_initial', '2022-01-21 05:57:10.934215'),
(3, 'admin', '0001_initial', '2022-01-21 05:57:11.068936'),
(4, 'admin', '0002_logentry_remove_auto_add', '2022-01-21 05:57:11.077740'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2022-01-21 05:57:11.085740'),
(6, 'contenttypes', '0002_remove_content_type_name', '2022-01-21 05:57:11.172587'),
(7, 'auth', '0002_alter_permission_name_max_length', '2022-01-21 05:57:11.222461'),
(8, 'auth', '0003_alter_user_email_max_length', '2022-01-21 05:57:11.256043'),
(9, 'auth', '0004_alter_user_username_opts', '2022-01-21 05:57:11.264045'),
(10, 'auth', '0005_alter_user_last_login_null', '2022-01-21 05:57:11.309996'),
(11, 'auth', '0006_require_contenttypes_0002', '2022-01-21 05:57:11.312897'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2022-01-21 05:57:11.319595'),
(13, 'auth', '0008_alter_user_username_max_length', '2022-01-21 05:57:11.370911'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2022-01-21 05:57:11.417104'),
(15, 'auth', '0010_alter_group_name_max_length', '2022-01-21 05:57:11.438109'),
(16, 'auth', '0011_update_proxy_permissions', '2022-01-21 05:57:11.446111'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2022-01-21 05:57:11.494698'),
(18, 'bodega', '0001_initial', '2022-01-21 05:57:11.656309'),
(19, 'bodega', '0002_usuario_nombres', '2022-01-21 05:57:11.695318'),
(20, 'sessions', '0001_initial', '2022-01-21 05:57:11.728326');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('rkfbnawhrx8126s0hk32x713u8pxjdzt', '.eJxVjjsOgzAMQK9SZa4i8qEJTFV3ph4AOcFA2pBIBCbE3Rsqhnbx4Pf85I20sC5juyacW9eRmjBy_d0ZsG8MB-heEIZIbQzL7Aw9FHrSRJvYoX-c7l9ghDTmazQaRGWlVYXBspQGueFSCGsrzVnPS1VwxTUo1Cixr4QRVaFUKXt9Y4xBjvo4uEDqjRx_sivBCZzPaegmF-7fSa3PYoiTmTFl1LhhRX95gncBEtn3D7qaTfc:1nAnJt:EzOB6YFNAYG_4oNNnMkq6uoamDj3m-P1EPUyGljM7Zk', '2022-02-04 06:22:45.438947');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `bodega_bodega`
--
ALTER TABLE `bodega_bodega`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `bodega_bodegaproducto`
--
ALTER TABLE `bodega_bodegaproducto`
  ADD PRIMARY KEY (`id`),
  ADD KEY `bodega_bodegaproducto_idBodega_id_7b398d22_fk_bodega_bodega_id` (`idBodega_id`),
  ADD KEY `bodega_bodegaproduct_idProducto_id_866aa40c_fk_bodega_pr` (`idProducto_id`);

--
-- Indices de la tabla `bodega_producto`
--
ALTER TABLE `bodega_producto`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `bodega_usuario`
--
ALTER TABLE `bodega_usuario`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `bodega_bodega`
--
ALTER TABLE `bodega_bodega`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `bodega_bodegaproducto`
--
ALTER TABLE `bodega_bodegaproducto`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `bodega_producto`
--
ALTER TABLE `bodega_producto`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `bodega_usuario`
--
ALTER TABLE `bodega_usuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `bodega_bodegaproducto`
--
ALTER TABLE `bodega_bodegaproducto`
  ADD CONSTRAINT `bodega_bodegaproduct_idProducto_id_866aa40c_fk_bodega_pr` FOREIGN KEY (`idProducto_id`) REFERENCES `bodega_producto` (`id`),
  ADD CONSTRAINT `bodega_bodegaproducto_idBodega_id_7b398d22_fk_bodega_bodega_id` FOREIGN KEY (`idBodega_id`) REFERENCES `bodega_bodega` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
