---
dataset_id: roedovre_buildings
semantic_domain: Built Environment / Structures
provenance: Datafordeleren - GeoDanmark Vektor (GEODKV_Bygning)
temporal_validity: 2026-04-25T13:00:00Z (Point-in-time snapshot)
spatial_extent: Rødovre Municipality, Denmark
data_type: vector (Polygon)
format: GeoJSON
coordinate_reference_system: EPSG:4326 (converted from EPSG:25832)
---

# Rødovre Buildings (Bygning)

## Description
This dataset contains the authoritative footprint polygons of buildings (`Bygning`) in Rødovre Municipality, extracted from the official GeoDanmark Vektor database via Datafordeleren's GraphQL API.

## Genesis Protocol
1. **API Selection:** Used Datafordeleren's GraphQL endpoint (`https://graphql.datafordeler.dk/GEODKV/v1`).
2. **Boundary Definition:** Queried OpenStreetMap via OSMnx for the administrative boundary of Rødovre Municipality.
3. **Bounding Box Strategy:** To circumvent the "Max GraphQL request size" limitation caused by complex polygon WKT strings, the exact boundary was converted into its envelope bounding box (`EPSG:25832`).
4. **Data Extraction:** Sent paginated GraphQL requests targeting the `GEODKV_Bygning` entity, using a spatial `intersects` filter with the bounding box WKT.
5. **Clipping:** Downloaded features were converted to `EPSG:4326` and strictly clipped using the exact administrative boundary polygon of Rødovre Municipality to discard features from neighboring municipalities that fell within the bounding box.

## Semantic Note
This dataset acts as a direct realisation of the `Built Structures` leaf node within the SPHERE architecture. It enables detailed density calculations, built-environment analysis, and spatial planning operations.
