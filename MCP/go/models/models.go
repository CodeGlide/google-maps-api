package models

import (
	"context"
	"github.com/mark3labs/mcp-go/mcp"
)

type Tool struct {
	Definition mcp.Tool
	Handler    func(ctx context.Context, req mcp.CallToolRequest) (*mcp.CallToolResult, error)
}

// GoogleMapsPlacesV1Place represents the GoogleMapsPlacesV1Place schema from the OpenAPI specification
type GoogleMapsPlacesV1Place struct {
	Iconmaskbaseuri string `json:"iconMaskBaseUri,omitempty"` // A truncated URL to an icon mask. User can access different icon type by appending type suffix to the end (eg, ".svg" or ".png").
	Name string `json:"name,omitempty"` // This Place's resource name, in `places/{place_id}` format. Can be used to look up the Place.
	Types []string `json:"types,omitempty"` // A set of type tags for this result. For example, "political" and "locality". For the complete list of possible values, see Table A and Table B at https://developers.google.com/maps/documentation/places/web-service/place-types
	Primarytypedisplayname GoogleTypeLocalizedText `json:"primaryTypeDisplayName,omitempty"` // Localized variant of a text in a particular language.
	Websiteuri string `json:"websiteUri,omitempty"` // The authoritative website for this place, e.g. a business' homepage. Note that for places that are part of a chain (e.g. an IKEA store), this will usually be the website for the individual store, not the overall chain.
	Internationalphonenumber string `json:"internationalPhoneNumber,omitempty"` // A human-readable phone number for the place, in international format.
	Pluscode GoogleMapsPlacesV1PlacePlusCode `json:"plusCode,omitempty"` // Plus code (http://plus.codes) is a location reference with two formats: global code defining a 14mx14m (1/8000th of a degree) or smaller rectangle, and compound code, replacing the prefix with a reference location.
	Serveswine bool `json:"servesWine,omitempty"` // Specifies if the place serves wine.
	Businessstatus string `json:"businessStatus,omitempty"` // The business status for the place.
	Parkingoptions GoogleMapsPlacesV1PlaceParkingOptions `json:"parkingOptions,omitempty"` // Information about parking options for the place. A parking lot could support more than one option at the same time.
	Servesbreakfast bool `json:"servesBreakfast,omitempty"` // Specifies if the place serves breakfast.
	Curbsidepickup bool `json:"curbsidePickup,omitempty"` // Specifies if the business supports curbside pickup.
	Editorialsummary GoogleTypeLocalizedText `json:"editorialSummary,omitempty"` // Localized variant of a text in a particular language.
	Primarytype string `json:"primaryType,omitempty"` // The primary type of the given result. This type must one of the Places API supported types. For example, "restaurant", "cafe", "airport", etc. A place can only have a single primary type. For the complete list of possible values, see Table A and Table B at https://developers.google.com/maps/documentation/places/web-service/place-types
	Addresscomponents []GoogleMapsPlacesV1PlaceAddressComponent `json:"addressComponents,omitempty"` // Repeated components for each locality level. Note the following facts about the address_components[] array: - The array of address components may contain more components than the formatted_address. - The array does not necessarily include all the political entities that contain an address, apart from those included in the formatted_address. To retrieve all the political entities that contain a specific address, you should use reverse geocoding, passing the latitude/longitude of the address as a parameter to the request. - The format of the response is not guaranteed to remain the same between requests. In particular, the number of address_components varies based on the address requested and can change over time for the same address. A component can change position in the array. The type of the component can change. A particular component may be missing in a later response.
	Servescocktails bool `json:"servesCocktails,omitempty"` // Place serves cocktails.
	Goodforgroups bool `json:"goodForGroups,omitempty"` // Place accommodates groups.
	Attributions []GoogleMapsPlacesV1PlaceAttribution `json:"attributions,omitempty"` // A set of data provider that must be shown with this result.
	Servesbeer bool `json:"servesBeer,omitempty"` // Specifies if the place serves beer.
	Goodforwatchingsports bool `json:"goodForWatchingSports,omitempty"` // Place is suitable for watching sports.
	Googlemapsuri string `json:"googleMapsUri,omitempty"` // A URL providing more information about this place.
	Servesvegetarianfood bool `json:"servesVegetarianFood,omitempty"` // Specifies if the place serves vegetarian food.
	Restroom bool `json:"restroom,omitempty"` // Place has restroom.
	Menuforchildren bool `json:"menuForChildren,omitempty"` // Place has a children's menu.
	Reservable bool `json:"reservable,omitempty"` // Specifies if the place supports reservations.
	Fueloptions GoogleMapsPlacesV1FuelOptions `json:"fuelOptions,omitempty"` // The most recent information about fuel options in a gas station. This information is updated regularly.
	Subdestinations []GoogleMapsPlacesV1PlaceSubDestination `json:"subDestinations,omitempty"` // A list of sub destinations related to the place.
	Utcoffsetminutes int `json:"utcOffsetMinutes,omitempty"` // Number of minutes this place's timezone is currently offset from UTC. This is expressed in minutes to support timezones that are offset by fractions of an hour, e.g. X hours and 15 minutes.
	Accessibilityoptions GoogleMapsPlacesV1PlaceAccessibilityOptions `json:"accessibilityOptions,omitempty"` // Information about the accessibility options a place offers.
	Adrformataddress string `json:"adrFormatAddress,omitempty"` // The place's address in adr microformat: http://microformats.org/wiki/adr.
	Photos []GoogleMapsPlacesV1Photo `json:"photos,omitempty"` // Information (including references) about photos of this place. A maximum of 10 photos can be returned.
	Formattedaddress string `json:"formattedAddress,omitempty"` // A full, human-readable address for this place.
	Regularopeninghours GoogleMapsPlacesV1PlaceOpeningHours `json:"regularOpeningHours,omitempty"` // Information about business hour of the place.
	Evchargeoptions GoogleMapsPlacesV1EVChargeOptions `json:"evChargeOptions,omitempty"` // Information about the EV Charge Station hosted in Place. Terminology follows https://afdc.energy.gov/fuels/electricity_infrastructure.html One port could charge one car at a time. One port has one or more connectors. One station has one or more ports.
	Id string `json:"id,omitempty"` // The unique identifier of a place.
	Regularsecondaryopeninghours []GoogleMapsPlacesV1PlaceOpeningHours `json:"regularSecondaryOpeningHours,omitempty"` // Contains an array of entries for information about regular secondary hours of a business. Secondary hours are different from a business's main hours. For example, a restaurant can specify drive through hours or delivery hours as its secondary hours. This field populates the type subfield, which draws from a predefined list of opening hours types (such as DRIVE_THROUGH, PICKUP, or TAKEOUT) based on the types of the place.
	Servescoffee bool `json:"servesCoffee,omitempty"` // Place serves coffee.
	Allowsdogs bool `json:"allowsDogs,omitempty"` // Place allows dogs.
	Servesdinner bool `json:"servesDinner,omitempty"` // Specifies if the place serves dinner.
	Goodforchildren bool `json:"goodForChildren,omitempty"` // Place is good for children.
	Servesdessert bool `json:"servesDessert,omitempty"` // Place serves dessert.
	Currentsecondaryopeninghours []GoogleMapsPlacesV1PlaceOpeningHours `json:"currentSecondaryOpeningHours,omitempty"` // Contains an array of entries for the next seven days including information about secondary hours of a business. Secondary hours are different from a business's main hours. For example, a restaurant can specify drive through hours or delivery hours as its secondary hours. This field populates the type subfield, which draws from a predefined list of opening hours types (such as DRIVE_THROUGH, PICKUP, or TAKEOUT) based on the types of the place. This field includes the special_days subfield of all hours, set for dates that have exceptional hours.
	Outdoorseating bool `json:"outdoorSeating,omitempty"` // Place provides outdoor seating.
	Rating float64 `json:"rating,omitempty"` // A rating between 1.0 and 5.0, based on user reviews of this place.
	Location GoogleTypeLatLng `json:"location,omitempty"` // An object that represents a latitude/longitude pair. This is expressed as a pair of doubles to represent degrees latitude and degrees longitude. Unless specified otherwise, this object must conform to the WGS84 standard. Values must be within normalized ranges.
	Livemusic bool `json:"liveMusic,omitempty"` // Place provides live music.
	Shortformattedaddress string `json:"shortFormattedAddress,omitempty"` // A short, human-readable address for this place.
	Userratingcount int `json:"userRatingCount,omitempty"` // The total number of reviews (with or without text) for this place.
	Reviews []GoogleMapsPlacesV1Review `json:"reviews,omitempty"` // List of reviews about this place, sorted by relevance. A maximum of 5 reviews can be returned.
	Viewport GoogleGeoTypeViewport `json:"viewport,omitempty"` // A latitude-longitude viewport, represented as two diagonally opposite `low` and `high` points. A viewport is considered a closed region, i.e. it includes its boundary. The latitude bounds must range between -90 to 90 degrees inclusive, and the longitude bounds must range between -180 to 180 degrees inclusive. Various cases include: - If `low` = `high`, the viewport consists of that single point. - If `low.longitude` > `high.longitude`, the longitude range is inverted (the viewport crosses the 180 degree longitude line). - If `low.longitude` = -180 degrees and `high.longitude` = 180 degrees, the viewport includes all longitudes. - If `low.longitude` = 180 degrees and `high.longitude` = -180 degrees, the longitude range is empty. - If `low.latitude` > `high.latitude`, the latitude range is empty. Both `low` and `high` must be populated, and the represented box cannot be empty (as specified by the definitions above). An empty viewport will result in an error. For example, this viewport fully encloses New York City: { "low": { "latitude": 40.477398, "longitude": -74.259087 }, "high": { "latitude": 40.91618, "longitude": -73.70018 } }
	Displayname GoogleTypeLocalizedText `json:"displayName,omitempty"` // Localized variant of a text in a particular language.
	Nationalphonenumber string `json:"nationalPhoneNumber,omitempty"` // A human-readable phone number for the place, in national format.
	Paymentoptions GoogleMapsPlacesV1PlacePaymentOptions `json:"paymentOptions,omitempty"` // Payment options the place accepts.
	Servesbrunch bool `json:"servesBrunch,omitempty"` // Specifies if the place serves brunch.
	Delivery bool `json:"delivery,omitempty"` // Specifies if the business supports delivery.
	Serveslunch bool `json:"servesLunch,omitempty"` // Specifies if the place serves lunch.
	Iconbackgroundcolor string `json:"iconBackgroundColor,omitempty"` // Background color for icon_mask in hex format, e.g. #909CE1.
	Currentopeninghours GoogleMapsPlacesV1PlaceOpeningHours `json:"currentOpeningHours,omitempty"` // Information about business hour of the place.
	Pricelevel string `json:"priceLevel,omitempty"` // Price level of the place.
	Takeout bool `json:"takeout,omitempty"` // Specifies if the business supports takeout.
	Dinein bool `json:"dineIn,omitempty"` // Specifies if the business supports indoor or outdoor seating options.
}

// GoogleMapsPlacesV1AutocompletePlacesResponseSuggestion represents the GoogleMapsPlacesV1AutocompletePlacesResponseSuggestion schema from the OpenAPI specification
type GoogleMapsPlacesV1AutocompletePlacesResponseSuggestion struct {
	Placeprediction GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionPlacePrediction `json:"placePrediction,omitempty"` // Prediction results for a Place Autocomplete prediction.
	Queryprediction GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionQueryPrediction `json:"queryPrediction,omitempty"` // Prediction results for a Query Autocomplete prediction.
}

// GoogleMapsPlacesV1PlaceAddressComponent represents the GoogleMapsPlacesV1PlaceAddressComponent schema from the OpenAPI specification
type GoogleMapsPlacesV1PlaceAddressComponent struct {
	Types []string `json:"types,omitempty"` // An array indicating the type(s) of the address component.
	Languagecode string `json:"languageCode,omitempty"` // The language used to format this components, in CLDR notation.
	Longtext string `json:"longText,omitempty"` // The full text description or name of the address component. For example, an address component for the country Australia may have a long_name of "Australia".
	Shorttext string `json:"shortText,omitempty"` // An abbreviated textual name for the address component, if available. For example, an address component for the country of Australia may have a short_name of "AU".
}

// GoogleMapsPlacesV1SearchNearbyResponse represents the GoogleMapsPlacesV1SearchNearbyResponse schema from the OpenAPI specification
type GoogleMapsPlacesV1SearchNearbyResponse struct {
	Places []GoogleMapsPlacesV1Place `json:"places,omitempty"` // A list of places that meets user's requirements like places types, number of places and specific location restriction.
}

// GoogleMapsPlacesV1SearchTextRequest represents the GoogleMapsPlacesV1SearchTextRequest schema from the OpenAPI specification
type GoogleMapsPlacesV1SearchTextRequest struct {
	Languagecode string `json:"languageCode,omitempty"` // Place details will be displayed with the preferred language if available. If the language code is unspecified or unrecognized, place details of any language may be returned, with a preference for English if such details exist. Current list of supported languages: https://developers.google.com/maps/faq#languagesupport.
	Locationbias interface{} `json:"locationBias,omitempty"` // The region to search. This location serves as a bias which means results around given location might be returned.
	Minrating float64 `json:"minRating,omitempty"` // Filter out results whose average user rating is strictly less than this limit. A valid value must be a float between 0 and 5 (inclusively) at a 0.5 cadence i.e. [0, 0.5, 1.0, ... , 5.0] inclusively. The input rating will round up to the nearest 0.5(ceiling). For instance, a rating of 0.6 will eliminate all results with a less than 1.0 rating.
	Opennow bool `json:"openNow,omitempty"` // Used to restrict the search to places that are currently open. The default is false.
	Pricelevels []string `json:"priceLevels,omitempty"` // Used to restrict the search to places that are marked as certain price levels. Users can choose any combinations of price levels. Default to select all price levels.
	Textquery string `json:"textQuery,omitempty"` // Required. The text query for textual search.
	Maxresultcount int `json:"maxResultCount,omitempty"` // Maximum number of results to return. It must be between 1 and 20, inclusively. The default is 20. If the number is unset, it falls back to the upper limit. If the number is set to negative or exceeds the upper limit, an INVALID_ARGUMENT error is returned.
	Rankpreference string `json:"rankPreference,omitempty"` // How results will be ranked in the response.
	Stricttypefiltering bool `json:"strictTypeFiltering,omitempty"` // Used to set strict type filtering for included_type. If set to true, only results of the same type will be returned. Default to false.
	Locationrestriction GoogleMapsPlacesV1SearchTextRequestLocationRestriction `json:"locationRestriction,omitempty"` // The region to search. This location serves as a restriction which means results outside given location will not be returned.
	Regioncode string `json:"regionCode,omitempty"` // The Unicode country/region code (CLDR) of the location where the request is coming from. This parameter is used to display the place details, like region-specific place name, if available. The parameter can affect results based on applicable law. For more information, see https://www.unicode.org/cldr/charts/latest/supplemental/territory_language_information.html. Note that 3-digit region codes are not currently supported.
	Includedtype string `json:"includedType,omitempty"` // The requested place type. Full list of types supported: https://developers.google.com/maps/documentation/places/web-service/place-types. Only support one included type.
}

// GoogleMapsPlacesV1PlacePaymentOptions represents the GoogleMapsPlacesV1PlacePaymentOptions schema from the OpenAPI specification
type GoogleMapsPlacesV1PlacePaymentOptions struct {
	Acceptscashonly bool `json:"acceptsCashOnly,omitempty"` // Place accepts cash only as payment. Places with this attribute may still accept other payment methods.
	Acceptscreditcards bool `json:"acceptsCreditCards,omitempty"` // Place accepts credit cards as payment.
	Acceptsdebitcards bool `json:"acceptsDebitCards,omitempty"` // Place accepts debit cards as payment.
	Acceptsnfc bool `json:"acceptsNfc,omitempty"` // Place accepts NFC payments.
}

// GoogleTypeLocalizedText represents the GoogleTypeLocalizedText schema from the OpenAPI specification
type GoogleTypeLocalizedText struct {
	Languagecode string `json:"languageCode,omitempty"` // The text's BCP-47 language code, such as "en-US" or "sr-Latn". For more information, see http://www.unicode.org/reports/tr35/#Unicode_locale_identifier.
	Text string `json:"text,omitempty"` // Localized string in the language corresponding to language_code below.
}

// GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionStructuredFormat represents the GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionStructuredFormat schema from the OpenAPI specification
type GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionStructuredFormat struct {
	Maintext GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionFormattableText `json:"mainText,omitempty"` // Text representing a Place or query prediction. The text may be used as is or formatted.
	Secondarytext GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionFormattableText `json:"secondaryText,omitempty"` // Text representing a Place or query prediction. The text may be used as is or formatted.
}

// GoogleMapsPlacesV1SearchTextResponse represents the GoogleMapsPlacesV1SearchTextResponse schema from the OpenAPI specification
type GoogleMapsPlacesV1SearchTextResponse struct {
	Places []GoogleMapsPlacesV1Place `json:"places,omitempty"` // A list of places that meet the user's text search criteria.
}

// GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionStringRange represents the GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionStringRange schema from the OpenAPI specification
type GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionStringRange struct {
	Endoffset int `json:"endOffset,omitempty"` // Zero-based offset of the last Unicode character (exclusive).
	Startoffset int `json:"startOffset,omitempty"` // Zero-based offset of the first Unicode character of the string (inclusive).
}

// GoogleMapsPlacesV1EVChargeOptionsConnectorAggregation represents the GoogleMapsPlacesV1EVChargeOptionsConnectorAggregation schema from the OpenAPI specification
type GoogleMapsPlacesV1EVChargeOptionsConnectorAggregation struct {
	Count int `json:"count,omitempty"` // Number of connectors in this aggregation.
	Maxchargeratekw float64 `json:"maxChargeRateKw,omitempty"` // The static max charging rate in kw of each connector in the aggregation.
	Outofservicecount int `json:"outOfServiceCount,omitempty"` // Number of connectors in this aggregation that are currently out of service.
	TypeField string `json:"type,omitempty"` // The connector type of this aggregation.
	Availabilitylastupdatetime string `json:"availabilityLastUpdateTime,omitempty"` // The timestamp when the connector availability information in this aggregation was last updated.
	Availablecount int `json:"availableCount,omitempty"` // Number of connectors in this aggregation that are currently available.
}

// GoogleMapsPlacesV1Circle represents the GoogleMapsPlacesV1Circle schema from the OpenAPI specification
type GoogleMapsPlacesV1Circle struct {
	Center GoogleTypeLatLng `json:"center,omitempty"` // An object that represents a latitude/longitude pair. This is expressed as a pair of doubles to represent degrees latitude and degrees longitude. Unless specified otherwise, this object must conform to the WGS84 standard. Values must be within normalized ranges.
	Radius float64 `json:"radius,omitempty"` // Required. Radius measured in meters. The radius must be within [0.0, 50000.0].
}

// GoogleMapsPlacesV1PlaceOpeningHoursSpecialDay represents the GoogleMapsPlacesV1PlaceOpeningHoursSpecialDay schema from the OpenAPI specification
type GoogleMapsPlacesV1PlaceOpeningHoursSpecialDay struct {
	Date GoogleTypeDate `json:"date,omitempty"` // Represents a whole or partial calendar date, such as a birthday. The time of day and time zone are either specified elsewhere or are insignificant. The date is relative to the Gregorian Calendar. This can represent one of the following: * A full date, with non-zero year, month, and day values. * A month and day, with a zero year (for example, an anniversary). * A year on its own, with a zero month and a zero day. * A year and month, with a zero day (for example, a credit card expiration date). Related types: * google.type.TimeOfDay * google.type.DateTime * google.protobuf.Timestamp
}

// GoogleTypeMoney represents the GoogleTypeMoney schema from the OpenAPI specification
type GoogleTypeMoney struct {
	Currencycode string `json:"currencyCode,omitempty"` // The three-letter currency code defined in ISO 4217.
	Nanos int `json:"nanos,omitempty"` // Number of nano (10^-9) units of the amount. The value must be between -999,999,999 and +999,999,999 inclusive. If `units` is positive, `nanos` must be positive or zero. If `units` is zero, `nanos` can be positive, zero, or negative. If `units` is negative, `nanos` must be negative or zero. For example $-1.75 is represented as `units`=-1 and `nanos`=-750,000,000.
	Units string `json:"units,omitempty"` // The whole units of the amount. For example if `currencyCode` is `"USD"`, then 1 unit is one US dollar.
}

// GoogleMapsPlacesV1EVChargeOptions represents the GoogleMapsPlacesV1EVChargeOptions schema from the OpenAPI specification
type GoogleMapsPlacesV1EVChargeOptions struct {
	Connectoraggregation []GoogleMapsPlacesV1EVChargeOptionsConnectorAggregation `json:"connectorAggregation,omitempty"` // A list of EV charging connector aggregations that contain connectors of the same type and same charge rate.
	Connectorcount int `json:"connectorCount,omitempty"` // Number of connectors at this station. However, because some ports can have multiple connectors but only be able to charge one car at a time (e.g.) the number of connectors may be greater than the total number of cars which can charge simultaneously.
}

// GoogleTypeDate represents the GoogleTypeDate schema from the OpenAPI specification
type GoogleTypeDate struct {
	Day int `json:"day,omitempty"` // Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn't significant.
	Month int `json:"month,omitempty"` // Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day.
	Year int `json:"year,omitempty"` // Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year.
}

// GoogleMapsPlacesV1PlaceOpeningHoursPeriod represents the GoogleMapsPlacesV1PlaceOpeningHoursPeriod schema from the OpenAPI specification
type GoogleMapsPlacesV1PlaceOpeningHoursPeriod struct {
	CloseField GoogleMapsPlacesV1PlaceOpeningHoursPeriodPoint `json:"close,omitempty"` // Status changing points.
	Open GoogleMapsPlacesV1PlaceOpeningHoursPeriodPoint `json:"open,omitempty"` // Status changing points.
}

// GoogleMapsPlacesV1PlaceAccessibilityOptions represents the GoogleMapsPlacesV1PlaceAccessibilityOptions schema from the OpenAPI specification
type GoogleMapsPlacesV1PlaceAccessibilityOptions struct {
	Wheelchairaccessibleentrance bool `json:"wheelchairAccessibleEntrance,omitempty"` // Places has wheelchair accessible entrance.
	Wheelchairaccessibleparking bool `json:"wheelchairAccessibleParking,omitempty"` // Place offers wheelchair accessible parking.
	Wheelchairaccessiblerestroom bool `json:"wheelchairAccessibleRestroom,omitempty"` // Place has wheelchair accessible restroom.
	Wheelchairaccessibleseating bool `json:"wheelchairAccessibleSeating,omitempty"` // Place has wheelchair accessible seating.
}

// GoogleMapsPlacesV1PhotoMedia represents the GoogleMapsPlacesV1PhotoMedia schema from the OpenAPI specification
type GoogleMapsPlacesV1PhotoMedia struct {
	Photouri string `json:"photoUri,omitempty"` // A short-lived uri that can be used to render the photo.
	Name string `json:"name,omitempty"` // The resource name of a photo media in the format: `places/{place_id}/photos/{photo_reference}/media`.
}

// GoogleTypeLatLng represents the GoogleTypeLatLng schema from the OpenAPI specification
type GoogleTypeLatLng struct {
	Latitude float64 `json:"latitude,omitempty"` // The latitude in degrees. It must be in the range [-90.0, +90.0].
	Longitude float64 `json:"longitude,omitempty"` // The longitude in degrees. It must be in the range [-180.0, +180.0].
}

// GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionPlacePrediction represents the GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionPlacePrediction schema from the OpenAPI specification
type GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionPlacePrediction struct {
	Placeid string `json:"placeId,omitempty"` // The unique identifier of the suggested Place. This identifier can be used in other APIs that accept Place IDs.
	Structuredformat GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionStructuredFormat `json:"structuredFormat,omitempty"` // Contains a breakdown of a Place or query prediction into main text and secondary text. For Place predictions, the main text contains the specific name of the Place. For query predictions, the main text contains the query. The secondary text contains additional disambiguating features (such as a city or region) to further identify the Place or refine the query.
	Text GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionFormattableText `json:"text,omitempty"` // Text representing a Place or query prediction. The text may be used as is or formatted.
	Types []string `json:"types,omitempty"` // List of types that apply to this Place from Table A or Table B in https://developers.google.com/maps/documentation/places/web-service/place-types. A type is a categorization of a Place. Places with shared types will share similar characteristics.
	Distancemeters int `json:"distanceMeters,omitempty"` // The length of the geodesic in meters from `origin` if `origin` is specified. Certain predictions such as routes may not populate this field.
	Place string `json:"place,omitempty"` // The resource name of the suggested Place. This name can be used in other APIs that accept Place names.
}

// GoogleMapsPlacesV1PlaceOpeningHoursPeriodPoint represents the GoogleMapsPlacesV1PlaceOpeningHoursPeriodPoint schema from the OpenAPI specification
type GoogleMapsPlacesV1PlaceOpeningHoursPeriodPoint struct {
	Date GoogleTypeDate `json:"date,omitempty"` // Represents a whole or partial calendar date, such as a birthday. The time of day and time zone are either specified elsewhere or are insignificant. The date is relative to the Gregorian Calendar. This can represent one of the following: * A full date, with non-zero year, month, and day values. * A month and day, with a zero year (for example, an anniversary). * A year on its own, with a zero month and a zero day. * A year and month, with a zero day (for example, a credit card expiration date). Related types: * google.type.TimeOfDay * google.type.DateTime * google.protobuf.Timestamp
	Day int `json:"day,omitempty"` // A day of the week, as an integer in the range 0-6. 0 is Sunday, 1 is Monday, etc.
	Hour int `json:"hour,omitempty"` // The hour in 2 digits. Ranges from 00 to 23.
	Minute int `json:"minute,omitempty"` // The minute in 2 digits. Ranges from 00 to 59.
	Truncated bool `json:"truncated,omitempty"` // Whether or not this endpoint was truncated. Truncation occurs when the real hours are outside the times we are willing to return hours between, so we truncate the hours back to these boundaries. This ensures that at most 24 * 7 hours from midnight of the day of the request are returned.
}

// GoogleMapsPlacesV1PlaceParkingOptions represents the GoogleMapsPlacesV1PlaceParkingOptions schema from the OpenAPI specification
type GoogleMapsPlacesV1PlaceParkingOptions struct {
	Paidgarageparking bool `json:"paidGarageParking,omitempty"` // Place offers paid garage parking.
	Paidparkinglot bool `json:"paidParkingLot,omitempty"` // Place offers paid parking lots.
	Paidstreetparking bool `json:"paidStreetParking,omitempty"` // Place offers paid street parking.
	Valetparking bool `json:"valetParking,omitempty"` // Place offers valet parking.
	Freegarageparking bool `json:"freeGarageParking,omitempty"` // Place offers free garage parking.
	Freeparkinglot bool `json:"freeParkingLot,omitempty"` // Place offers free parking lots.
	Freestreetparking bool `json:"freeStreetParking,omitempty"` // Place offers free street parking.
}

// GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionQueryPrediction represents the GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionQueryPrediction schema from the OpenAPI specification
type GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionQueryPrediction struct {
	Structuredformat GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionStructuredFormat `json:"structuredFormat,omitempty"` // Contains a breakdown of a Place or query prediction into main text and secondary text. For Place predictions, the main text contains the specific name of the Place. For query predictions, the main text contains the query. The secondary text contains additional disambiguating features (such as a city or region) to further identify the Place or refine the query.
	Text GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionFormattableText `json:"text,omitempty"` // Text representing a Place or query prediction. The text may be used as is or formatted.
}

// GoogleMapsPlacesV1Photo represents the GoogleMapsPlacesV1Photo schema from the OpenAPI specification
type GoogleMapsPlacesV1Photo struct {
	Authorattributions []GoogleMapsPlacesV1AuthorAttribution `json:"authorAttributions,omitempty"` // This photo's authors.
	Heightpx int `json:"heightPx,omitempty"` // The maximum available height, in pixels.
	Name string `json:"name,omitempty"` // Identifier. A reference representing this place photo which may be used to look up this place photo again (also called the API "resource" name: `places/{place_id}/photos/{photo}`).
	Widthpx int `json:"widthPx,omitempty"` // The maximum available width, in pixels.
}

// GoogleMapsPlacesV1AuthorAttribution represents the GoogleMapsPlacesV1AuthorAttribution schema from the OpenAPI specification
type GoogleMapsPlacesV1AuthorAttribution struct {
	Photouri string `json:"photoUri,omitempty"` // Profile photo URI of the author of the Photo or Review.
	Uri string `json:"uri,omitempty"` // URI of the author of the Photo or Review.
	Displayname string `json:"displayName,omitempty"` // Name of the author of the Photo or Review.
}

// GoogleMapsPlacesV1SearchTextRequestLocationRestriction represents the GoogleMapsPlacesV1SearchTextRequestLocationRestriction schema from the OpenAPI specification
type GoogleMapsPlacesV1SearchTextRequestLocationRestriction struct {
	Rectangle GoogleGeoTypeViewport `json:"rectangle,omitempty"` // A latitude-longitude viewport, represented as two diagonally opposite `low` and `high` points. A viewport is considered a closed region, i.e. it includes its boundary. The latitude bounds must range between -90 to 90 degrees inclusive, and the longitude bounds must range between -180 to 180 degrees inclusive. Various cases include: - If `low` = `high`, the viewport consists of that single point. - If `low.longitude` > `high.longitude`, the longitude range is inverted (the viewport crosses the 180 degree longitude line). - If `low.longitude` = -180 degrees and `high.longitude` = 180 degrees, the viewport includes all longitudes. - If `low.longitude` = 180 degrees and `high.longitude` = -180 degrees, the longitude range is empty. - If `low.latitude` > `high.latitude`, the latitude range is empty. Both `low` and `high` must be populated, and the represented box cannot be empty (as specified by the definitions above). An empty viewport will result in an error. For example, this viewport fully encloses New York City: { "low": { "latitude": 40.477398, "longitude": -74.259087 }, "high": { "latitude": 40.91618, "longitude": -73.70018 } }
}

// GoogleMapsPlacesV1PlaceSubDestination represents the GoogleMapsPlacesV1PlaceSubDestination schema from the OpenAPI specification
type GoogleMapsPlacesV1PlaceSubDestination struct {
	Id string `json:"id,omitempty"` // The place id of the sub destination.
	Name string `json:"name,omitempty"` // The resource name of the sub destination.
}

// GoogleMapsPlacesV1AutocompletePlacesRequest represents the GoogleMapsPlacesV1AutocompletePlacesRequest schema from the OpenAPI specification
type GoogleMapsPlacesV1AutocompletePlacesRequest struct {
	Sessiontoken string `json:"sessionToken,omitempty"` // Optional. A string which identifies an Autocomplete session for billing purposes. Must be a URL and filename safe base64 string with at most 36 ASCII characters in length. Otherwise an INVALID_ARGUMENT error is returned. The session begins when the user starts typing a query, and concludes when they select a place and a call to Place Details or Address Validation is made. Each session can have multiple queries, followed by one Place Details or Address Validation request. The credentials used for each request within a session must belong to the same Google Cloud Console project. Once a session has concluded, the token is no longer valid; your app must generate a fresh token for each session. If the `session_token` parameter is omitted, or if you reuse a session token, the session is charged as if no session token was provided (each request is billed separately). We recommend the following guidelines: * Use session tokens for all Place Autocomplete calls. * Generate a fresh token for each session. Using a version 4 UUID is recommended. * Ensure that the credentials used for all Place Autocomplete, Place Details, and Address Validation requests within a session belong to the same Cloud Console project. * Be sure to pass a unique session token for each new session. Using the same token for more than one session will result in each request being billed individually.
	Input string `json:"input,omitempty"` // Required. The text string on which to search.
	Locationbias interface{} `json:"locationBias,omitempty"` // The region to search. The results may be biased around the specified region.
	Locationrestriction interface{} `json:"locationRestriction,omitempty"` // The region to search. The results will be restricted to the specified region.
	Origin GoogleTypeLatLng `json:"origin,omitempty"` // An object that represents a latitude/longitude pair. This is expressed as a pair of doubles to represent degrees latitude and degrees longitude. Unless specified otherwise, this object must conform to the WGS84 standard. Values must be within normalized ranges.
	Regioncode string `json:"regionCode,omitempty"` // Optional. The region code, specified as a CLDR two-character region code. This affects address formatting, result ranking, and may influence what results are returned. This does not restrict results to the specified region. To restrict results to a region, use `region_code_restriction`.
	Includequerypredictions bool `json:"includeQueryPredictions,omitempty"` // Optional. If true, the response will include both Place and query predictions. Otherwise the response will only return Place predictions.
	Includedprimarytypes []string `json:"includedPrimaryTypes,omitempty"` // Optional. Included primary Place type (for example, "restaurant" or "gas_station") from https://developers.google.com/maps/documentation/places/web-service/place-types. A Place is only returned if its primary type is included in this list. Up to 5 values can be specified. If no types are specified, all Place types are returned.
	Languagecode string `json:"languageCode,omitempty"` // Optional. The language in which to return results. Defaults to en-US. The results may be in mixed languages if the language used in `input` is different from `language_code` or if the returned Place does not have a translation from the local language to `language_code`.
	Inputoffset int `json:"inputOffset,omitempty"` // Optional. A zero-based Unicode character offset of `input` indicating the cursor position in `input`. The cursor position may influence what predictions are returned. If empty, defaults to the length of `input`.
	Includedregioncodes []string `json:"includedRegionCodes,omitempty"` // Optional. Only include results in the specified regions, specified as up to 15 CLDR two-character region codes. An empty set will not restrict the results. If both `location_restriction` and `included_region_codes` are set, the results will be located in the area of intersection.
}

// GoogleMapsPlacesV1PlaceAttribution represents the GoogleMapsPlacesV1PlaceAttribution schema from the OpenAPI specification
type GoogleMapsPlacesV1PlaceAttribution struct {
	Provider string `json:"provider,omitempty"` // Name of the Place's data provider.
	Provideruri string `json:"providerUri,omitempty"` // URI to the Place's data provider.
}

// GoogleMapsPlacesV1PlaceOpeningHours represents the GoogleMapsPlacesV1PlaceOpeningHours schema from the OpenAPI specification
type GoogleMapsPlacesV1PlaceOpeningHours struct {
	Secondaryhourstype string `json:"secondaryHoursType,omitempty"` // A type string used to identify the type of secondary hours.
	Specialdays []GoogleMapsPlacesV1PlaceOpeningHoursSpecialDay `json:"specialDays,omitempty"` // Structured information for special days that fall within the period that the returned opening hours cover. Special days are days that could impact the business hours of a place, e.g. Christmas day. Set for current_opening_hours and current_secondary_opening_hours if there are exceptional hours.
	Weekdaydescriptions []string `json:"weekdayDescriptions,omitempty"` // Localized strings describing the opening hours of this place, one string for each day of the week. Will be empty if the hours are unknown or could not be converted to localized text. Example: "Sun: 18:00–06:00"
	Opennow bool `json:"openNow,omitempty"` // Is this place open right now? Always present unless we lack time-of-day or timezone data for these opening hours.
	Periods []GoogleMapsPlacesV1PlaceOpeningHoursPeriod `json:"periods,omitempty"` // The periods that this place is open during the week. The periods are in chronological order, starting with Sunday in the place-local timezone. An empty (but not absent) value indicates a place that is never open, e.g. because it is closed temporarily for renovations.
}

// GoogleMapsPlacesV1SearchNearbyRequest represents the GoogleMapsPlacesV1SearchNearbyRequest schema from the OpenAPI specification
type GoogleMapsPlacesV1SearchNearbyRequest struct {
	Rankpreference string `json:"rankPreference,omitempty"` // How results will be ranked in the response.
	Regioncode string `json:"regionCode,omitempty"` // The Unicode country/region code (CLDR) of the location where the request is coming from. This parameter is used to display the place details, like region-specific place name, if available. The parameter can affect results based on applicable law. For more information, see https://www.unicode.org/cldr/charts/latest/supplemental/territory_language_information.html. Note that 3-digit region codes are not currently supported.
	Excludedprimarytypes []string `json:"excludedPrimaryTypes,omitempty"` // Excluded primary Place type (e.g. "restaurant" or "gas_station") from https://developers.google.com/maps/documentation/places/web-service/place-types. Up to 50 types from [Table A](https://developers.google.com/maps/documentation/places/web-service/place-types#table-a) may be specified. If there are any conflicting primary types, i.e. a type appears in both included_primary_types and excluded_primary_types, an INVALID_ARGUMENT error is returned. If a Place type is specified with multiple type restrictions, only places that satisfy all of the restrictions are returned. For example, if we have {included_types = ["restaurant"], excluded_primary_types = ["restaurant"]}, the returned places provide "restaurant" related services but do not operate primarily as "restaurants".
	Excludedtypes []string `json:"excludedTypes,omitempty"` // Excluded Place type (eg, "restaurant" or "gas_station") from https://developers.google.com/maps/documentation/places/web-service/place-types. Up to 50 types from [Table A](https://developers.google.com/maps/documentation/places/web-service/place-types#table-a) may be specified. If the client provides both included_types (e.g. restaurant) and excluded_types (e.g. cafe), then the response should include places that are restaurant but not cafe. The response includes places that match at least one of the included_types and none of the excluded_types. If there are any conflicting types, i.e. a type appears in both included_types and excluded_types, an INVALID_ARGUMENT error is returned. If a Place type is specified with multiple type restrictions, only places that satisfy all of the restrictions are returned. For example, if we have {included_types = ["restaurant"], excluded_primary_types = ["restaurant"]}, the returned places provide "restaurant" related services but do not operate primarily as "restaurants".
	Includedtypes []string `json:"includedTypes,omitempty"` // Included Place type (eg, "restaurant" or "gas_station") from https://developers.google.com/maps/documentation/places/web-service/place-types. Up to 50 types from [Table A](https://developers.google.com/maps/documentation/places/web-service/place-types#table-a) may be specified. If there are any conflicting types, i.e. a type appears in both included_types and excluded_types, an INVALID_ARGUMENT error is returned. If a Place type is specified with multiple type restrictions, only places that satisfy all of the restrictions are returned. For example, if we have {included_types = ["restaurant"], excluded_primary_types = ["restaurant"]}, the returned places provide "restaurant" related services but do not operate primarily as "restaurants".
	Maxresultcount int `json:"maxResultCount,omitempty"` // Maximum number of results to return. It must be between 1 and 20 (default), inclusively. If the number is unset, it falls back to the upper limit. If the number is set to negative or exceeds the upper limit, an INVALID_ARGUMENT error is returned.
	Languagecode string `json:"languageCode,omitempty"` // Place details will be displayed with the preferred language if available. If the language code is unspecified or unrecognized, place details of any language may be returned, with a preference for English if such details exist. Current list of supported languages: https://developers.google.com/maps/faq#languagesupport.
	Locationrestriction GoogleMapsPlacesV1SearchNearbyRequestLocationRestriction `json:"locationRestriction,omitempty"` // The region to search.
	Includedprimarytypes []string `json:"includedPrimaryTypes,omitempty"` // Included primary Place type (e.g. "restaurant" or "gas_station") from https://developers.google.com/maps/documentation/places/web-service/place-types. A place can only have a single primary type from the supported types table associated with it. Up to 50 types from [Table A](https://developers.google.com/maps/documentation/places/web-service/place-types#table-a) may be specified. If there are any conflicting primary types, i.e. a type appears in both included_primary_types and excluded_primary_types, an INVALID_ARGUMENT error is returned. If a Place type is specified with multiple type restrictions, only places that satisfy all of the restrictions are returned. For example, if we have {included_types = ["restaurant"], excluded_primary_types = ["restaurant"]}, the returned places provide "restaurant" related services but do not operate primarily as "restaurants".
}

// GoogleMapsPlacesV1SearchNearbyRequestLocationRestriction represents the GoogleMapsPlacesV1SearchNearbyRequestLocationRestriction schema from the OpenAPI specification
type GoogleMapsPlacesV1SearchNearbyRequestLocationRestriction struct {
	Circle GoogleMapsPlacesV1Circle `json:"circle,omitempty"` // Circle with a LatLng as center and radius.
}

// GoogleMapsPlacesV1FuelOptionsFuelPrice represents the GoogleMapsPlacesV1FuelOptionsFuelPrice schema from the OpenAPI specification
type GoogleMapsPlacesV1FuelOptionsFuelPrice struct {
	TypeField string `json:"type,omitempty"` // The type of fuel.
	Updatetime string `json:"updateTime,omitempty"` // The time the fuel price was last updated.
	Price GoogleTypeMoney `json:"price,omitempty"` // Represents an amount of money with its currency type.
}

// GoogleMapsPlacesV1Review represents the GoogleMapsPlacesV1Review schema from the OpenAPI specification
type GoogleMapsPlacesV1Review struct {
	Originaltext GoogleTypeLocalizedText `json:"originalText,omitempty"` // Localized variant of a text in a particular language.
	Publishtime string `json:"publishTime,omitempty"` // Timestamp for the review.
	Rating float64 `json:"rating,omitempty"` // A number between 1.0 and 5.0, also called the number of stars.
	Relativepublishtimedescription string `json:"relativePublishTimeDescription,omitempty"` // A string of formatted recent time, expressing the review time relative to the current time in a form appropriate for the language and country.
	Text GoogleTypeLocalizedText `json:"text,omitempty"` // Localized variant of a text in a particular language.
	Authorattribution GoogleMapsPlacesV1AuthorAttribution `json:"authorAttribution,omitempty"` // Information about the author of the UGC data. Used in Photo, and Review.
	Name string `json:"name,omitempty"` // A reference representing this place review which may be used to look up this place review again (also called the API "resource" name: `places/{place_id}/reviews/{review}`).
}

// GoogleMapsPlacesV1AutocompletePlacesResponse represents the GoogleMapsPlacesV1AutocompletePlacesResponse schema from the OpenAPI specification
type GoogleMapsPlacesV1AutocompletePlacesResponse struct {
	Suggestions []GoogleMapsPlacesV1AutocompletePlacesResponseSuggestion `json:"suggestions,omitempty"` // Contains a list of suggestions, ordered in descending order of relevance.
}

// GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionFormattableText represents the GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionFormattableText schema from the OpenAPI specification
type GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionFormattableText struct {
	Text string `json:"text,omitempty"` // Text that may be used as is or formatted with `matches`.
	Matches []GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionStringRange `json:"matches,omitempty"` // A list of string ranges identifying where the input request matched in `text`. The ranges can be used to format specific parts of `text`. The substrings may not be exact matches of `input` if the matching was determined by criteria other than string matching (for example, spell corrections or transliterations). These values are Unicode character offsets of `text`. The ranges are guaranteed to be ordered in increasing offset values.
}

// GoogleMapsPlacesV1PlacePlusCode represents the GoogleMapsPlacesV1PlacePlusCode schema from the OpenAPI specification
type GoogleMapsPlacesV1PlacePlusCode struct {
	Globalcode string `json:"globalCode,omitempty"` // Place's global (full) code, such as "9FWM33GV+HQ", representing an 1/8000 by 1/8000 degree area (~14 by 14 meters).
	Compoundcode string `json:"compoundCode,omitempty"` // Place's compound code, such as "33GV+HQ, Ramberg, Norway", containing the suffix of the global code and replacing the prefix with a formatted name of a reference entity.
}

// GoogleGeoTypeViewport represents the GoogleGeoTypeViewport schema from the OpenAPI specification
type GoogleGeoTypeViewport struct {
	High GoogleTypeLatLng `json:"high,omitempty"` // An object that represents a latitude/longitude pair. This is expressed as a pair of doubles to represent degrees latitude and degrees longitude. Unless specified otherwise, this object must conform to the WGS84 standard. Values must be within normalized ranges.
	Low GoogleTypeLatLng `json:"low,omitempty"` // An object that represents a latitude/longitude pair. This is expressed as a pair of doubles to represent degrees latitude and degrees longitude. Unless specified otherwise, this object must conform to the WGS84 standard. Values must be within normalized ranges.
}

// GoogleMapsPlacesV1FuelOptions represents the GoogleMapsPlacesV1FuelOptions schema from the OpenAPI specification
type GoogleMapsPlacesV1FuelOptions struct {
	Fuelprices []GoogleMapsPlacesV1FuelOptionsFuelPrice `json:"fuelPrices,omitempty"` // The last known fuel price for each type of fuel this station has. There is one entry per fuel type this station has. Order is not important.
}
