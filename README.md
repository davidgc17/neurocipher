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
---

## 📂 Estructura del proyecto

```
neurocipher/
│
├── src/
│ ├── rsa_basic.py
│ ├── symmetric_encrypt.py
│ └── elliptic_curve.py
│
├── tests/
│ ├── test_rsa_basic.py
│ ├── test_symmetric_encrypt.py
│ └── test_elliptic_curve.py
│
├── demos/
│ ├── demo_symmetric.py
│ ├── demo_file_encryption.py
│ └── demo_ecdsa.py
│
├── keys/
│ └── (archivos de claves si se generan)
│
├── examples/
│ └── message.txt
│
├── requirements.txt
├── README.md
└── guia_neurocipher.pdf
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

-Fase 4: Integración con redes neuronales (Hopfield).

-Fase 5: Criptografía avanzada, gestión segura de claves y pruebas de robustez.

-Automatización de referencias académicas con Semantic Scholar.

-Actualización continua de la guía teórica en PDF.

---

## 📄 Licencia

Este proyecto se distribuye bajo la **Licencia Apache 2.0**.
