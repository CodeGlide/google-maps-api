package main

import (
	"github.com/places-api-new/mcp-server/config"
	"github.com/places-api-new/mcp-server/models"
	tools_places "github.com/places-api-new/mcp-server/tools/places"
)

func GetAll(cfg *config.APIConfig) []models.Tool {
	return []models.Tool{
		tools_places.CreatePlaces_places_searchnearbyTool(cfg),
		tools_places.CreatePlaces_places_searchtextTool(cfg),
		tools_places.CreatePlaces_places_photos_getmediaTool(cfg),
		tools_places.CreatePlaces_places_autocompleteTool(cfg),
	}
}
