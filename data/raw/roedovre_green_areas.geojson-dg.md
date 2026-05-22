---
dataset_id: roedovre_green_areas
semantic_domain: Natural Environment / Land Cover
provenance: Datafordeleren - GeoDanmark Vektor (GEODKV_Skov, GEODKV_KratBevoksning, GEODKV_Vaadomraade)
temporal_validity: 2026-04-25T13:00:00Z (Point-in-time snapshot)
spatial_extent: Rødovre Municipality, Denmark
data_type: vector (Polygon)
format: GeoJSON
coordinate_reference_system: EPSG:4326 (converted from EPSG:25832)
---

# Rødovre Green Areas (Skov, KratBevoksning, Vådområde)

## Description
This dataset aggregates authoritative representations of green and natural land covers—specifically forests (`Skov`), scrub/thickets (`KratBevoksning`), and wetlands (`Vådområde`)—within Rødovre Municipality. The data is extracted from the official GeoDanmark Vektor database via Datafordeleren's GraphQL API.

## Genesis Protocol
1. **API Selection:** Used Datafordeleren's GraphQL endpoint (`https://graphql.datafordeler.dk/GEODKV/v1`).
2. **Boundary Definition:** Queried OpenStreetMap via OSMnx for the administrative boundary of Rødovre Municipality.
3. **Bounding Box Strategy:** To circumvent the "Max GraphQL request size" limitation caused by complex polygon WKT strings, the exact boundary was converted into its envelope bounding box (`EPSG:25832`).
4. **Data Extraction:** Sent paginated GraphQL requests targeting the `GEODKV_Skov`, `GEODKV_KratBevoksning`, and `GEODKV_Vaadomraade` entities, using a spatial `intersects` filter with the bounding box WKT.
5. **Clipping:** Downloaded features were converted to `EPSG:4326` and strictly clipped using the exact administrative boundary polygon of Rødovre Municipality to discard features from neighboring municipalities that fell within the bounding box.
6. **Aggregation:** The three independent thematic layers were concatenated into a single GeoDataFrame and assigned a `layer` attribute to differentiate them, providing a unified "Green Areas" dataset.

## Semantic Note
This dataset acts as a direct realisation of the `Natural Environment / Land Cover` leaf node within the SPHERE architecture. It is essential for environmental impact assessments, green-space accessibility studies, and ecological corridor mapping.
