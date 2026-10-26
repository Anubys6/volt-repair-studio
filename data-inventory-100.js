// BASE DE DATOS DE 100 REFACCIONES REALES - VOLT REPAIR STUDIO
// Basado en costos de compra de proveedores mayoristas en México (FixOEM, Capital Móvil, Tech House, HL México)
// y precios al cliente final (sin mano de obra).

const inventory100 = [
  // ==========================================
  // PANTALLAS IPHONE (25 ÍTEMS)
  // ==========================================
  { id: 'REF-001', name: 'Pantalla Retina HD Incell', category: 'pantallas', model: 'iPhone 6 / 6s', costPrice: 190, salePrice: 450, stock: 4, minStock: 2 },
  { id: 'REF-002', name: 'Pantalla Retina HD Incell', category: 'pantallas', model: 'iPhone 7 / 8 / SE 2020', costPrice: 220, salePrice: 490, stock: 5, minStock: 2 },
  { id: 'REF-003', name: 'Pantalla Retina HD Plus', category: 'pantallas', model: 'iPhone 7 Plus / 8 Plus', costPrice: 260, salePrice: 550, stock: 3, minStock: 2 },
  { id: 'REF-004', name: 'Pantalla Hard OLED Super Retina', category: 'pantallas', model: 'iPhone X', costPrice: 420, salePrice: 950, stock: 4, minStock: 2 },
  { id: 'REF-005', name: 'Pantalla Liquid Retina Incell', category: 'pantallas', model: 'iPhone XR', costPrice: 380, salePrice: 850, stock: 6, minStock: 2 },
  { id: 'REF-006', name: 'Pantalla Hard OLED Super Retina', category: 'pantallas', model: 'iPhone XS', costPrice: 450, salePrice: 980, stock: 3, minStock: 1 },
  { id: 'REF-007', name: 'Pantalla Soft OLED Super Retina Max', category: 'pantallas', model: 'iPhone XS Max', costPrice: 580, salePrice: 1250, stock: 3, minStock: 1 },
  { id: 'REF-008', name: 'Pantalla Liquid Retina Incell HD', category: 'pantallas', model: 'iPhone 11', costPrice: 390, salePrice: 890, stock: 8, minStock: 3 },
  { id: 'REF-009', name: 'Pantalla Soft OLED Super Retina XDR', category: 'pantallas', model: 'iPhone 11 Pro', costPrice: 620, salePrice: 1390, stock: 4, minStock: 2 },
  { id: 'REF-010', name: 'Pantalla Soft OLED Super Retina XDR', category: 'pantallas', model: 'iPhone 11 Pro Max', costPrice: 750, salePrice: 1590, stock: 4, minStock: 2 },
  { id: 'REF-011', name: 'Pantalla Hard OLED Super Retina', category: 'pantallas', model: 'iPhone 12 mini', costPrice: 650, salePrice: 1390, stock: 2, minStock: 1 },
  { id: 'REF-012', name: 'Pantalla Hard OLED Super Retina XDR', category: 'pantallas', model: 'iPhone 12 / 12 Pro', costPrice: 690, salePrice: 1450, stock: 6, minStock: 2 },
  { id: 'REF-013', name: 'Pantalla Soft OLED Super Retina XDR', category: 'pantallas', model: 'iPhone 12 Pro Max', costPrice: 890, salePrice: 1850, stock: 3, minStock: 2 },
  { id: 'REF-014', name: 'Pantalla Hard OLED TrueTone', category: 'pantallas', model: 'iPhone 13 mini', costPrice: 720, salePrice: 1490, stock: 2, minStock: 1 },
  { id: 'REF-015', name: 'Pantalla Soft OLED Super Retina XDR', category: 'pantallas', model: 'iPhone 13', costPrice: 750, salePrice: 1550, stock: 5, minStock: 2 },
  { id: 'REF-016', name: 'Pantalla LTPO OLED 120Hz ProMotion', category: 'pantallas', model: 'iPhone 13 Pro', costPrice: 1450, salePrice: 2650, stock: 3, minStock: 1 },
  { id: 'REF-017', name: 'Pantalla LTPO OLED 120Hz ProMotion', category: 'pantallas', model: 'iPhone 13 Pro Max', costPrice: 1650, salePrice: 2950, stock: 2, minStock: 1 },
  { id: 'REF-018', name: 'Pantalla Soft OLED Super Retina XDR', category: 'pantallas', model: 'iPhone 14', costPrice: 820, salePrice: 1650, stock: 4, minStock: 2 },
  { id: 'REF-019', name: 'Pantalla Soft OLED Super Retina XDR', category: 'pantallas', model: 'iPhone 14 Plus', costPrice: 950, salePrice: 1850, stock: 2, minStock: 1 },
  { id: 'REF-020', name: 'Pantalla Dynamic Island OLED LTPO 120Hz', category: 'pantallas', model: 'iPhone 14 Pro', costPrice: 1750, salePrice: 3100, stock: 2, minStock: 1 },
  { id: 'REF-021', name: 'Pantalla Dynamic Island OLED LTPO 120Hz', category: 'pantallas', model: 'iPhone 14 Pro Max', costPrice: 1950, salePrice: 3450, stock: 2, minStock: 1 },
  { id: 'REF-022', name: 'Pantalla Dynamic Island OLED 2000nits', category: 'pantallas', model: 'iPhone 15', costPrice: 1100, salePrice: 2200, stock: 3, minStock: 1 },
  { id: 'REF-023', name: 'Pantalla Dynamic Island OLED 2000nits', category: 'pantallas', model: 'iPhone 15 Plus', costPrice: 1250, salePrice: 2450, stock: 2, minStock: 1 },
  { id: 'REF-024', name: 'Pantalla Titanium ProMotion 120Hz', category: 'pantallas', model: 'iPhone 15 Pro', costPrice: 2200, salePrice: 3800, stock: 1, minStock: 1 },
  { id: 'REF-025', name: 'Pantalla Titanium ProMotion 120Hz', category: 'pantallas', model: 'iPhone 15 Pro Max', costPrice: 2450, salePrice: 4200, stock: 1, minStock: 1 },

  // ==========================================
  // PANTALLAS SAMSUNG GALAXY (20 ÍTEMS)
  // ==========================================
  { id: 'REF-026', name: 'Pantalla PLS LCD con Marco', category: 'pantallas', model: 'Samsung Galaxy A03 / A04 / A04e', costPrice: 220, salePrice: 550, stock: 5, minStock: 2 },
  { id: 'REF-027', name: 'Pantalla PLS LCD 90Hz con Marco', category: 'pantallas', model: 'Samsung Galaxy A05 / A05s', costPrice: 250, salePrice: 590, stock: 4, minStock: 2 },
  { id: 'REF-028', name: 'Pantalla PLS LCD Incell con Marco', category: 'pantallas', model: 'Samsung Galaxy A12 / A13 4G', costPrice: 260, salePrice: 620, stock: 6, minStock: 2 },
  { id: 'REF-029', name: 'Pantalla PLS LCD 90Hz FHD+', category: 'pantallas', model: 'Samsung Galaxy A14 4G / 5G', costPrice: 290, salePrice: 680, stock: 5, minStock: 2 },
  { id: 'REF-030', name: 'Pantalla Super AMOLED 90Hz', category: 'pantallas', model: 'Samsung Galaxy A15 4G / 5G', costPrice: 380, salePrice: 850, stock: 4, minStock: 2 },
  { id: 'REF-031', name: 'Pantalla Super AMOLED 90Hz con Marco', category: 'pantallas', model: 'Samsung Galaxy A22 4G / A23', costPrice: 420, salePrice: 920, stock: 3, minStock: 2 },
  { id: 'REF-032', name: 'Pantalla Super AMOLED 90Hz FHD+', category: 'pantallas', model: 'Samsung Galaxy A24 / A25 5G', costPrice: 460, salePrice: 990, stock: 3, minStock: 1 },
  { id: 'REF-033', name: 'Pantalla Super AMOLED 120Hz', category: 'pantallas', model: 'Samsung Galaxy A33 5G / A34 5G', costPrice: 580, salePrice: 1250, stock: 4, minStock: 2 },
  { id: 'REF-034', name: 'Pantalla Super AMOLED 120Hz HDR', category: 'pantallas', model: 'Samsung Galaxy A35 5G', costPrice: 650, salePrice: 1390, stock: 2, minStock: 1 },
  { id: 'REF-035', name: 'Pantalla Super AMOLED FHD+ con Marco', category: 'pantallas', model: 'Samsung Galaxy A51 / A52 4G/5G', costPrice: 520, salePrice: 1150, stock: 5, minStock: 2 },
  { id: 'REF-036', name: 'Pantalla Super AMOLED 120Hz con Marco', category: 'pantallas', model: 'Samsung Galaxy A53 5G', costPrice: 620, salePrice: 1350, stock: 4, minStock: 2 },
  { id: 'REF-037', name: 'Pantalla Super AMOLED 120Hz Vision Booster', category: 'pantallas', model: 'Samsung Galaxy A54 5G', costPrice: 720, salePrice: 1550, stock: 4, minStock: 2 },
  { id: 'REF-038', name: 'Pantalla Super AMOLED 120Hz Armor', category: 'pantallas', model: 'Samsung Galaxy A55 5G', costPrice: 880, salePrice: 1800, stock: 2, minStock: 1 },
  { id: 'REF-039', name: 'Pantalla Dynamic AMOLED 2X 120Hz', category: 'pantallas', model: 'Samsung Galaxy S20 FE / S21 FE', costPrice: 680, salePrice: 1450, stock: 4, minStock: 2 },
  { id: 'REF-040', name: 'Pantalla Dynamic AMOLED 2X 120Hz', category: 'pantallas', model: 'Samsung Galaxy S21 5G / S21+ 5G', costPrice: 850, salePrice: 1750, stock: 3, minStock: 1 },
  { id: 'REF-041', name: 'Pantalla Dynamic AMOLED 2X Curva', category: 'pantallas', model: 'Samsung Galaxy S21 Ultra 5G', costPrice: 1650, salePrice: 2950, stock: 2, minStock: 1 },
  { id: 'REF-042', name: 'Pantalla Dynamic AMOLED 2X 1300nits', category: 'pantallas', model: 'Samsung Galaxy S22 5G / S22+', costPrice: 990, salePrice: 1980, stock: 3, minStock: 1 },
  { id: 'REF-043', name: 'Pantalla Dynamic AMOLED 2X Edge con Marco', category: 'pantallas', model: 'Samsung Galaxy S22 Ultra 5G', costPrice: 1850, salePrice: 3350, stock: 2, minStock: 1 },
  { id: 'REF-044', name: 'Pantalla Dynamic AMOLED 2X 1750nits', category: 'pantallas', model: 'Samsung Galaxy S23 5G / S23+', costPrice: 1250, salePrice: 2400, stock: 2, minStock: 1 },
  { id: 'REF-045', name: 'Pantalla Dynamic AMOLED 2X Gorilla Armor', category: 'pantallas', model: 'Samsung Galaxy S23 Ultra / S24 Ultra', costPrice: 2200, salePrice: 3900, stock: 2, minStock: 1 },

  // ==========================================
  // PANTALLAS MOTOROLA (15 ÍTEMS)
  // ==========================================
  { id: 'REF-046', name: 'Pantalla IPS LCD con Marco', category: 'pantallas', model: 'Moto E13 / E20 / E22 / E32', costPrice: 210, salePrice: 520, stock: 5, minStock: 2 },
  { id: 'REF-047', name: 'Pantalla IPS LCD 90Hz con Marco', category: 'pantallas', model: 'Moto G13 / G14 / G23', costPrice: 240, salePrice: 580, stock: 4, minStock: 2 },
  { id: 'REF-048', name: 'Pantalla IPS LCD 90Hz', category: 'pantallas', model: 'Moto G20 / G30 / G31', costPrice: 240, salePrice: 580, stock: 4, minStock: 2 },
  { id: 'REF-049', name: 'Pantalla OLED FHD+ Max Vision', category: 'pantallas', model: 'Moto G41 / G42', costPrice: 360, salePrice: 820, stock: 3, minStock: 1 },
  { id: 'REF-050', name: 'Pantalla OLED 90Hz con Marco', category: 'pantallas', model: 'Moto G52', costPrice: 380, salePrice: 850, stock: 4, minStock: 2 },
  { id: 'REF-051', name: 'Pantalla IPS LCD 120Hz', category: 'pantallas', model: 'Moto G53 / G54 5G', costPrice: 320, salePrice: 750, stock: 6, minStock: 2 },
  { id: 'REF-052', name: 'Pantalla IPS LCD 120Hz FHD+', category: 'pantallas', model: 'Moto G60 / G60s', costPrice: 350, salePrice: 790, stock: 4, minStock: 2 },
  { id: 'REF-053', name: 'Pantalla OLED 120Hz HDR10', category: 'pantallas', model: 'Moto G71 5G / G72', costPrice: 410, salePrice: 890, stock: 3, minStock: 1 },
  { id: 'REF-054', name: 'Pantalla IPS LCD 120Hz', category: 'pantallas', model: 'Moto G73 5G', costPrice: 390, salePrice: 860, stock: 3, minStock: 1 },
  { id: 'REF-055', name: 'Pantalla pOLED 120Hz 10-bit', category: 'pantallas', model: 'Moto G84 5G', costPrice: 480, salePrice: 1050, stock: 5, minStock: 2 },
  { id: 'REF-056', name: 'Pantalla OLED 144Hz HDR10+', category: 'pantallas', model: 'Moto Edge 20 / 20 Pro', costPrice: 650, salePrice: 1350, stock: 2, minStock: 1 },
  { id: 'REF-057', name: 'Pantalla OLED 144Hz con Marco', category: 'pantallas', model: 'Moto Edge 30 / 30 Neo', costPrice: 720, salePrice: 1480, stock: 3, minStock: 1 },
  { id: 'REF-058', name: 'Pantalla Curva pOLED 144Hz Endless', category: 'pantallas', model: 'Moto Edge 40 / 40 Neo', costPrice: 890, salePrice: 1780, stock: 2, minStock: 1 },
  { id: 'REF-059', name: 'Pantalla Curva Super HD 144Hz', category: 'pantallas', model: 'Moto Edge 50 Pro / Ultra', costPrice: 1200, salePrice: 2300, stock: 2, minStock: 1 },
  { id: 'REF-060', name: 'Pantalla OLED 120Hz con Marco', category: 'pantallas', model: 'Moto G82 5G', costPrice: 440, salePrice: 960, stock: 3, minStock: 1 },

  // ==========================================
  // PANTALLAS XIAOMI / POCO / HONOR (10 ÍTEMS)
  // ==========================================
  { id: 'REF-061', name: 'Pantalla AMOLED 120Hz con Marco', category: 'pantallas', model: 'Xiaomi Redmi Note 10 / 10 Pro', costPrice: 460, salePrice: 980, stock: 4, minStock: 2 },
  { id: 'REF-062', name: 'Pantalla AMOLED 90Hz FHD+', category: 'pantallas', model: 'Xiaomi Redmi Note 11 / 11S', costPrice: 480, salePrice: 1020, stock: 5, minStock: 2 },
  { id: 'REF-063', name: 'Pantalla AMOLED 120Hz 1200nits', category: 'pantallas', model: 'Xiaomi Redmi Note 12 / 12S', costPrice: 510, salePrice: 1090, stock: 4, minStock: 2 },
  { id: 'REF-064', name: 'Pantalla AMOLED 120Hz CrystalRes', category: 'pantallas', model: 'Xiaomi Redmi Note 13 / 13 Pro 5G', costPrice: 590, salePrice: 1250, stock: 3, minStock: 2 },
  { id: 'REF-065', name: 'Pantalla IPS LCD 120Hz HDR10', category: 'pantallas', model: 'POCO X3 NFC / X3 Pro', costPrice: 350, salePrice: 790, stock: 5, minStock: 2 },
  { id: 'REF-066', name: 'Pantalla AMOLED 120Hz Flow', category: 'pantallas', model: 'POCO X4 Pro 5G / X5 Pro 5G', costPrice: 560, salePrice: 1190, stock: 3, minStock: 1 },
  { id: 'REF-067', name: 'Pantalla AMOLED 120Hz Dolby Vision', category: 'pantallas', model: 'POCO F4 / F5 5G', costPrice: 720, salePrice: 1490, stock: 2, minStock: 1 },
  { id: 'REF-068', name: 'Pantalla CrystalRes AMOLED 144Hz', category: 'pantallas', model: 'Xiaomi 12T / 13T Pro', costPrice: 850, salePrice: 1750, stock: 2, minStock: 1 },
  { id: 'REF-069', name: 'Pantalla IPS LCD 90Hz / OLED', category: 'pantallas', model: 'Honor X7 / X8 / X9', costPrice: 380, salePrice: 850, stock: 3, minStock: 1 },
  { id: 'REF-070', name: 'Pantalla Curva OLED 120Hz Ultra Resistente', category: 'pantallas', model: 'Honor Magic 5 Lite / 6 Lite', costPrice: 780, salePrice: 1600, stock: 3, minStock: 1 },

  // ==========================================
  // BATERÍAS CERTIFICADAS LI-ION (15 ÍTEMS)
  // ==========================================
  { id: 'REF-071', name: 'Batería Li-Ion Grado A+ (1821mAh)', category: 'baterias', model: 'iPhone 8 / SE 2020 / SE 2022', costPrice: 130, salePrice: 350, stock: 6, minStock: 2 },
  { id: 'REF-072', name: 'Batería Li-Ion Grado A+ (2716mAh)', category: 'baterias', model: 'iPhone X', costPrice: 170, salePrice: 420, stock: 4, minStock: 2 },
  { id: 'REF-073', name: 'Batería Li-Ion Grado A+ (2942mAh)', category: 'baterias', model: 'iPhone XR', costPrice: 180, salePrice: 440, stock: 6, minStock: 2 },
  { id: 'REF-074', name: 'Batería Li-Ion Grado A+ (3110mAh) Sin Avisos', category: 'baterias', model: 'iPhone 11', costPrice: 220, salePrice: 490, stock: 8, minStock: 3 },
  { id: 'REF-075', name: 'Batería Li-Ion Grado A+ (3046mAh) Sin Avisos', category: 'baterias', model: 'iPhone 11 Pro', costPrice: 240, salePrice: 510, stock: 5, minStock: 2 },
  { id: 'REF-076', name: 'Batería Li-Ion Grado A+ (3969mAh) Sin Avisos', category: 'baterias', model: 'iPhone 11 Pro Max', costPrice: 260, salePrice: 540, stock: 5, minStock: 2 },
  { id: 'REF-077', name: 'Batería Li-Ion Grado A+ (2815mAh) BMS Preparado', category: 'baterias', model: 'iPhone 12 / 12 Pro', costPrice: 240, salePrice: 520, stock: 6, minStock: 2 },
  { id: 'REF-078', name: 'Batería Li-Ion Grado A+ (3687mAh) BMS Preparado', category: 'baterias', model: 'iPhone 12 Pro Max', costPrice: 270, salePrice: 570, stock: 4, minStock: 2 },
  { id: 'REF-079', name: 'Batería Li-Ion Grado A+ (3227mAh) Chip Original', category: 'baterias', model: 'iPhone 13 / 13 Pro', costPrice: 280, salePrice: 590, stock: 5, minStock: 2 },
  { id: 'REF-080', name: 'Batería Li-Ion Grado A+ (4352mAh) Chip Original', category: 'baterias', model: 'iPhone 13 Pro Max', costPrice: 310, salePrice: 650, stock: 4, minStock: 2 },
  { id: 'REF-081', name: 'Batería Li-Ion Grado A+ (3279mAh) BMS Prep', category: 'baterias', model: 'iPhone 14 / 14 Pro', costPrice: 320, salePrice: 680, stock: 4, minStock: 2 },
  { id: 'REF-082', name: 'Batería Li-Ion Grado A+ (4323mAh) BMS Prep', category: 'baterias', model: 'iPhone 14 Pro Max', costPrice: 360, salePrice: 740, stock: 3, minStock: 2 },
  { id: 'REF-083', name: 'Batería Li-Ion Grado A+ (3349mAh)', category: 'baterias', model: 'iPhone 15 / 15 Pro', costPrice: 390, salePrice: 790, stock: 3, minStock: 1 },
  { id: 'REF-084', name: 'Batería Samsung 5000mAh EB-BA536ABY', category: 'baterias', model: 'Samsung Galaxy A53 / A54 / A34', costPrice: 170, salePrice: 420, stock: 6, minStock: 2 },
  { id: 'REF-085', name: 'Batería Moto 5000mAh TurboPower MC50', category: 'baterias', model: 'Moto G50 / G60 / G54 / G84', costPrice: 160, salePrice: 390, stock: 7, minStock: 2 },

  // ==========================================
  // TAPAS TRASERAS CRISTAL MAGSAFE (8 ÍTEMS)
  // ==========================================
  { id: 'REF-086', name: 'Tapa Trasera Cristal Agujero Grande', category: 'tapas', model: 'iPhone 8 / SE 2020', costPrice: 80, salePrice: 220, stock: 4, minStock: 1 },
  { id: 'REF-087', name: 'Tapa Trasera Cristal Templado', category: 'tapas', model: 'iPhone X / XR / XS', costPrice: 95, salePrice: 250, stock: 5, minStock: 2 },
  { id: 'REF-088', name: 'Tapa Trasera Cristal Mate / Brillante', category: 'tapas', model: 'iPhone 11 / 11 Pro / 11 Pro Max', costPrice: 120, salePrice: 290, stock: 6, minStock: 2 },
  { id: 'REF-089', name: 'Tapa Trasera Cristal MagSafe OEM', category: 'tapas', model: 'iPhone 12 / 12 Pro', costPrice: 140, salePrice: 340, stock: 5, minStock: 2 },
  { id: 'REF-090', name: 'Tapa Trasera Cristal MagSafe OEM', category: 'tapas', model: 'iPhone 13 / 13 Pro / 13 Pro Max', costPrice: 160, salePrice: 380, stock: 6, minStock: 2 },
  { id: 'REF-091', name: 'Tapa Trasera Cristal Desmontable OEM', category: 'tapas', model: 'iPhone 14 / 14 Plus / 14 Pro', costPrice: 190, salePrice: 440, stock: 4, minStock: 2 },
  { id: 'REF-092', name: 'Tapa Trasera Cristal Infundido Color / Titanio', category: 'tapas', model: 'iPhone 15 / 15 Pro / 15 Pro Max', costPrice: 260, salePrice: 580, stock: 3, minStock: 1 },
  { id: 'REF-093', name: 'Tapa Trasera Cristal Original con Lente', category: 'tapas', model: 'Samsung Galaxy S22 / S23 / S24 Ultra', costPrice: 180, salePrice: 420, stock: 4, minStock: 2 },

  // ==========================================
  // FLEXORES DE CARGA, CÁMARAS & QUÍMICOS (7 ÍTEMS)
  // ==========================================
  { id: 'REF-094', name: 'Flexor Puerto Carga Lightning + Micrófono', category: 'flexores', model: 'iPhone 11 / 11 Pro', costPrice: 110, salePrice: 290, stock: 5, minStock: 2 },
  { id: 'REF-095', name: 'Flexor Puerto Carga Lightning + Antena', category: 'flexores', model: 'iPhone 12 / 12 Pro', costPrice: 140, salePrice: 350, stock: 4, minStock: 2 },
  { id: 'REF-096', name: 'Flexor Puerto Carga Lightning Original OEM', category: 'flexores', model: 'iPhone 13 / 13 Pro', costPrice: 160, salePrice: 390, stock: 4, minStock: 2 },
  { id: 'REF-097', name: 'Flexor Puerto Carga USB-C + Micrófono', category: 'flexores', model: 'iPhone 15 / 15 Pro', costPrice: 230, salePrice: 490, stock: 3, minStock: 1 },
  { id: 'REF-098', name: 'Subplaca Pin de Carga Rápida USB-C', category: 'flexores', model: 'Samsung Galaxy A53 / A54 / S21', costPrice: 90, salePrice: 260, stock: 6, minStock: 2 },
  { id: 'REF-099', name: 'Módulo Cámara Trasera 48MP con Estabilizador OIS', category: 'camaras', model: 'iPhone 14 Pro / 14 Pro Max', costPrice: 650, salePrice: 1150, stock: 2, minStock: 1 },
  { id: 'REF-100', name: 'Kit Químicos Pegamento B-7000 (110ml) + Cintas Térmicas', category: 'quimicos', model: 'Universal iPhone / Android', costPrice: 45, salePrice: 120, stock: 12, minStock: 3 }
];

if (typeof module !== 'undefined' && module.exports) {
  module.exports = inventory100;
}
