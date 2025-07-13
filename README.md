# 🧠🔐 Neurocipher

**Neurocipher** es un proyecto de investigación y desarrollo en criptografía aplicada y ciberseguridad, combinando herramientas clásicas como RSA con técnicas modernas como el cifrado simétrico (AES/Fernet), con el objetivo de explorar su integración futura con redes neuronales y sistemas adaptativos.

---

## 📌 Fases del proyecto

### ✅ FASE 1 — Cifrado Asimétrico (RSA)
- Implementación manual de funciones clave:
  - `gcd()`, `modinv()`, `generate_keys()`, `encrypt_message()`, `decrypt_message()`
- Test unitarios cubriendo todos los casos.
- Documentación detallada y guía PDF incluida.

### ✅ FASE 2 — Cifrado Simétrico (Fernet)
- Cifrado y descifrado de mensajes.
- Cifrado y descifrado de archivos `.txt`.
- Uso de claves simétricas generadas de forma segura.
- Pruebas con demos ejecutables.

---

## 📂 Estructura del proyecto

```
neurocipher/
│
├── src/
│   ├── rsa_basic.py
│   └── symmetric_encrypt.py
│
├── tests/
│   ├── test_rsa_basic.py
│   └── test_symmetric_encrypt.py
│
├── demos/
│   ├── demo_symmetric.py
│   └── demo_file_encryption.py
│
├── keys/
│   └── (archivos de claves si se generan)
│
├── examples/
│   └── message.txt (ejemplo de texto a cifrar)
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

- FASE 3: Integración con redes neuronales (Hopfield).
- FASE 4: Criptografía avanzada y pruebas de robustez.
- Referencias automatizadas con Semantic Scholar.
- Exportación de manual técnico en PDF (funciones y teoría).

---

## 📄 Licencia

Este proyecto se distribuye bajo la **Licencia Apache 2.0**.
