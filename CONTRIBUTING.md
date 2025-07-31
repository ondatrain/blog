# 🎯 Guía de Contribución al Blog OndaTrain

¡Gracias por considerar contribuir a nuestro blog! 🙌 Este proyecto se nutre del conocimiento colectivo de la comunidad. Aquí encontrarás todo lo necesario para colaborar efectivamente.

```python
if not contributor_engaged:
    print("¡Tu experiencia es valiosa aquí!")
else:
    print("🚀 Prepárate para compartir tu conocimiento con la comunidad")
```

## 🌱 ¿Cómo puedo contribuir?

### 1. 📝 Nuevos Artículos/Tutoriales
- Propón temas en [Issues](https://github.com/ondatrain/blog/issues)
- Mantén un tono técnico pero accesible

### 2. ✏️ Correcciones y Mejoras
- ¿Encontraste un error técnico? ¡Házlo saber!
- ¿Sabes una mejor manera de explicar un concepto?
- ¿Las muestras de código pueden optimizarse?

### 3. 🌍 Traducciones
- Actualmente trabajando en soporte para:
  - Inglés

### 4. 🛠️ Mejoras Técnicas
- ¿Ves oportunidades en el código del blog?
- ¿Mejoras de performance?

## 🛠️ Proceso de Contribución
1. **Crea un fork** del repositorio
2. **Clona tu fork** localmente:
   ```bash
   git clone https://github.com/tu-usuario/blog.git
   ```
3. **Crea una rama descriptiva**:
   ```bash
   git checkout -b feat/add-llm-caching-article
   ```
4. **Haz commits atómicos** con mensajes claros:
   ```bash
   git commit -m "docs: add section about FastAPI middleware"
   ```
5. **Envía un Pull Request** desde tu fork

## 📌 Convenciones

### Estructura de Archivos
```
/content
  /es
    /articles
      /fastapi-llm-integration.md
  /en
    /tutorials
      /django-orm-advanced.md
```

### Formato de Artículos
- Usa Markdown con frontmatter para metadata
- Incluye ejemplos de código ejecutables
- Añade diagramas (Mermaid/ASCII) cuando sea útil
- Referencia fuentes/autorías apropiadamente

### Código de Conducta
Respetamos el [Código de Conducta Contributor Covenant](CODE_OF_CONDUCT.md). Por favor:
- Sé amable y profesional
- Critica ideas, no personas
- Mantén discusiones técnicas

## 🔍 Revisión de PRs

Nuestro flujo:
1. Un maintainer revisará tu PR en 48h
2. Puede sugerir cambios (etiquetados como "suggestions")
3. Una vez aprobado, se mergeará a la rama `develop`
4. Se publicará en el próximo ciclo (semanal)

## 🏷️ Sistema de Etiquetas

| Etiqueta       | Descripción                          |
|----------------|--------------------------------------|
| `docs`         | Mejoras documentación                |
| `tutorial`     | Nuevos tutoriales                    |
| `translation`  | Contribuciones de traducción         |
| `bug`          | Corrección de errores                |
| `enhancement`  | Mejoras de contenido existente       |

## ❓ ¿Necesitas ayuda?

- Abre un [Issue](https://github.com/ondatrain/blog/issues)

---

✨ *El conocimiento compartido es oro digital* 

¡Gracias por hacer del blog On da Train un recurso más valioso para la comunidad! 🎉