package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func main() {
	// Crea una instancia del enrutador Gin
	r := gin.Default()

	// Define una ruta GET simple
	r.GET("/api/hola", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{
			"mensaje": "¡Hola, mundo!",
		})
	})

	// Inicia el servidor en el puerto 8080
	r.Run(":8080")
}
