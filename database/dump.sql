-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 31-Ago-2023 às 16:14
-- Versão do servidor: 10.4.27-MariaDB
-- versão do PHP: 8.0.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `sanderson`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `empresa`
--

CREATE TABLE `empresa` (
  `id` int(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `link` varchar(255) NOT NULL,
  `nome` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `logs`
--

CREATE TABLE `logs` (
  `id` int(11) NOT NULL,
  `time` varchar(255) DEFAULT NULL,
  `description` varchar(2000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `relatorio_0004`
--

CREATE TABLE `relatorio_0004` (
  `id` int(11) NOT NULL,
  `cliente` varchar(255) DEFAULT NULL,
  `codigo` varchar(255) DEFAULT NULL,
  `aniversario` varchar(255) DEFAULT NULL,
  `telefone` varchar(255) DEFAULT NULL,
  `celular` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `sexo` varchar(255) DEFAULT NULL,
  `como_conheceu` varchar(255) DEFAULT NULL,
  `cpf` varchar(255) DEFAULT NULL,
  `cep` varchar(255) DEFAULT NULL,
  `endereco` varchar(255) DEFAULT NULL,
  `numero` varchar(255) DEFAULT NULL,
  `estado` varchar(255) DEFAULT NULL,
  `cidade` varchar(255) DEFAULT NULL,
  `complemento` varchar(255) DEFAULT NULL,
  `bairro` varchar(255) DEFAULT NULL,
  `profissao` varchar(255) DEFAULT NULL,
  `cadastrado` varchar(255) DEFAULT NULL,
  `obs` varchar(255) DEFAULT NULL,
  `rg` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `relatorio_0053`
--

CREATE TABLE `relatorio_0053` (
  `id` int(11) NOT NULL,
  `data_reserva` varchar(255) DEFAULT NULL,
  `hora` varchar(255) DEFAULT NULL,
  `cliente` varchar(255) DEFAULT NULL,
  `servico` varchar(255) DEFAULT NULL,
  `valor` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `relatorio_0063`
--

CREATE TABLE `relatorio_0063` (
  `id` int(11) NOT NULL,
  `cliente` varchar(255) DEFAULT NULL,
  `pacote` varchar(255) DEFAULT NULL,
  `servico` varchar(255) DEFAULT NULL,
  `total` int(11) DEFAULT NULL,
  `utilizados` int(11) DEFAULT NULL,
  `validade` varchar(255) DEFAULT NULL,
  `compra` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `relatorio_0123`
--

CREATE TABLE `relatorio_0123` (
  `id` int(11) NOT NULL,
  `profissional` varchar(255) DEFAULT NULL,
  `tipo_contratacao` varchar(255) DEFAULT NULL,
  `cargo` varchar(255) DEFAULT NULL,
  `banco` varchar(255) DEFAULT NULL,
  `agencia` varchar(255) DEFAULT NULL,
  `conta` varchar(255) DEFAULT NULL,
  `faturado` decimal(10,2) DEFAULT NULL,
  `rateio_servicos` decimal(10,2) DEFAULT NULL,
  `rateio_produtos` decimal(10,2) DEFAULT NULL,
  `rateio_outros` decimal(10,2) DEFAULT NULL,
  `caixinha` decimal(10,2) DEFAULT NULL,
  `descontos` decimal(10,2) DEFAULT NULL,
  `a_pagar` decimal(10,2) DEFAULT NULL,
  `valor_casa` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `relatorio_0186`
--

CREATE TABLE `relatorio_0186` (
  `id` int(11) NOT NULL,
  `data` varchar(255) DEFAULT NULL,
  `comanda` varchar(255) DEFAULT NULL,
  `item` varchar(255) DEFAULT NULL,
  `tipo` varchar(255) DEFAULT NULL,
  `categoria` varchar(255) DEFAULT NULL,
  `profissional` varchar(255) DEFAULT NULL,
  `assistente_1` varchar(255) DEFAULT NULL,
  `assistente_2` varchar(255) DEFAULT NULL,
  `comissao_percentual` decimal(10,2) DEFAULT NULL,
  `cliente` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `telefone` varchar(255) DEFAULT NULL,
  `celular` varchar(255) DEFAULT NULL,
  `valor` decimal(10,2) DEFAULT NULL,
  `desconto` decimal(10,2) DEFAULT NULL,
  `quantidade` varchar(255) DEFAULT NULL,
  `custo` decimal(10,2) DEFAULT NULL,
  `comissao` decimal(10,2) DEFAULT NULL,
  `liquido` decimal(10,2) DEFAULT NULL,
  `ua` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `empresa`
--
ALTER TABLE `empresa`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `logs`
--
ALTER TABLE `logs`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `relatorio_0004`
--
ALTER TABLE `relatorio_0004`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `relatorio_0053`
--
ALTER TABLE `relatorio_0053`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `relatorio_0063`
--
ALTER TABLE `relatorio_0063`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `relatorio_0123`
--
ALTER TABLE `relatorio_0123`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `relatorio_0186`
--
ALTER TABLE `relatorio_0186`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `empresa`
--
ALTER TABLE `empresa`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `logs`
--
ALTER TABLE `logs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de tabela `relatorio_0004`
--
ALTER TABLE `relatorio_0004`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7850;

--
-- AUTO_INCREMENT de tabela `relatorio_0053`
--
ALTER TABLE `relatorio_0053`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4172;

--
-- AUTO_INCREMENT de tabela `relatorio_0063`
--
ALTER TABLE `relatorio_0063`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=146;

--
-- AUTO_INCREMENT de tabela `relatorio_0123`
--
ALTER TABLE `relatorio_0123`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=145;

--
-- AUTO_INCREMENT de tabela `relatorio_0186`
--
ALTER TABLE `relatorio_0186`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3819;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
