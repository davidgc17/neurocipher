# 🧠🔐 Neurocipher

**Neurocipher** es un proyecto de investigación y desarrollo en criptografía aplicada y ciberseguridad, combinando herramientas clásicas como RSA con técnicas modernas como el cifrado simétrico (AES/Fernet), con el objetivo de explorar su integración futura con redes neuronales y sistemas adaptativos.

---

## 📌 Fases del proyecto

### Fase 1 — Criptografía Asimétrica (RSA básico)

- Implementación manual de funciones clave: `gcd()`, `modinv()`, `generate_keys()`, `encrypt_message()`, `decrypt_message()`.
- Pruebas unitarias completas.
- Documentación detallada con guía en PDF incluida.

### Fase 2 — Criptografía Simétrica (Fernet)

- Cifrado y descifrado de mensajes y archivos `.txt`.
- Uso de claves simétricas generadas de forma segura.
- Demos ejecutables y pruebas.

### Fase 3 — Criptografía con Curvas Elípticas (ECC) y Firma Digital (ECDSA)

- Implementación propia de curvas elípticas y operaciones de grupo.
- Generación de claves ECC.
- Firma y verificación digital con ECDSA.
- Cálculo dinámico del orden del punto generador.
- Documentación matemática y código con pruebas.

### Fase 4 — Redes de Hopfield para recuperación de claves (v1.0 a v1.3-A)

- **v1.0**: Red Hopfield básica entrenada con una sola clave.
- **v1.1**: Soporte para múltiples patrones (entrenamiento con 3 claves simultáneas).
- **v1.2**: Preentrenamiento mediante annealing (ruido decreciente) para mejorar la generalización.
- **v1.3-A**: Entrenamiento reforzado con patrones ruidosos + repeticiones + actualización en bloques. Alta robustez incluso con ruido del 25–50 %.
- Resultados almacenados en CSV y graficados con scripts en `graficos/`.
- Documentación detallada en LaTeX (`guia_hopfield.tex`).

---

## 📂 Estructura del proyecto

```
neurocipher/
│
├── src/                     # Código fuente principal
│ ├── rsa_basic.py
│ ├── symmetric_encrypt.py
│ ├── elliptic_curve.py
│ ├── Hopfield_net.py
│ └── secure_key_utils.py
│
├── tests/                   # Tests unitarios
│ ├── test_rsa_basic.py
│ ├── test_symmetric_encrypt.py
│ └── test_elliptic_curve.py
│
├── demos/                   # Demos ejecutables
│ ├── demo_symmetric.py
│ ├── demo_file_encryption.py
│ └── demo_ecdsa.py
│
├── graficos/                # Scripts y resultados gráficos
│
├── logs/                    # Resultados en CSV de recuperación Hopfield
│
├── keys/                    # Archivos de claves generadas
│
├── examples/                # Archivos de ejemplo
│ └── message.txt
│
├── guia_neurocipher.pdf     # Guía general del proyecto
├── guia_hopfield.tex        # Documento LaTeX sobre redes de Hopfield
├── requirements.txt
└── README.md
```

---

## 🛠️ Instalación

```bash
git clone https://github.com/tuusuario/neurocipher.git
cd neurocipher
pip install -r requirements.txt
```

---

## 🚀 Uso rápido

```bash
# Ejemplo: ejecutar la demo de cifrado de mensajes
python demos/demo_symmetric.py

# Ejemplo: cifrar y descifrar archivo de texto
python demos/demo_file_encryption.py
```

---

## 🧪 Ejecutar tests

```bash
make test
```

---

## 🧩 Próximos pasos

- Fase 5: Criptografía avanzada, recuperación parcial y gestión segura de claves.
- Implementación final de integración clave-criptograma.
- Automatización de referencias académicas con Semantic Scholar.
- Actualización completa de documentación en PDF.

---

## 📄 Licencia

Este proyecto se distribuye bajo la **Licencia Apache 2.0**.

