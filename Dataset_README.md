
# Catalonia Building Energy-Efficiency Certificates (EPC) Dataset Open Data Catalonia · Catalan Energy Institute (ICAEN)


##  Context and Motivation  
Energy use in buildings is one of the European Union’s largest climate-mitigation levers.  
- **2002 → 2010 → 2012 Directives** (EPBD 2002/91/EC, recast 2010/31/EU, EED 2012/27/EU) made **Energy Performance Certificates (EPCs)** mandatory for all real-estate transactions.  
- **Spain** transposed the EPBD in **2007** for new builds (RD 47/2007) and in **2013** for the existing stock (RD 235/2013).  
- Since **1 June 2013** every new, sold, or rented dwelling in **Catalonia** must be rated from **A (best) to G (worst)** for both energy use and CO₂ emissions.  

Catalonia’s EPC register has therefore become an unparalleled longitudinal record of building-stock efficiency, retrofit uptake, and renewable-system diffusion.
---

##  Dataset Provenance  
| Property | Detail |
|----------|--------|
| **Publisher** | Catalan Energy Institute (ICAEN) |
| **Open-data host** | [analisi.transparenciacatalunya.cat](https://analisi.transparenciacatalunya.cat) |
| **Initial release** | 7 May 2019 |
| **Last data refresh** | 30 Apr 2025 |
| **Update cadence** | **Weekly** (new certificates + metadata fixes) |
| **Rows (2025-05 snapshot)** | **≈ 1 340 000** certificates |
| **Columns** | **69** (see full schema below) |
| **Spatial scope** | All 947 Catalan municipalities; WGS 84 geocodes + UTM |
| **Temporal scope** | EPCs issued **2007 – present** (earliest build years ~ 1850) |
| **Licence** | “Open Data BCN” terms · no usage fee · citation required |

> ⚠ **Note** Certificates are **self-reported by qualified assessors**; some fields may be missing or estimated.

---

## What Each Record Contains  

### 1 Core identifiers and location  
- `NUM_CASE` (unique certificate ID)  
- Full address & cadastral reference  
- Municipality / county / province codes  
- Precise **latitude / longitude** in WGS 84  

### 2 Headline ratings  
| Field | Description | Scale |
|-------|-------------|-------|
| `consumer_qualification_d` | **Non-renewable primary energy rating** | **A–G** |
| `emissions_rating` | **CO₂-emissions rating** | **A–G** |

### 3 Quantitative performance  
- `non_renewable_primary_energy` (kWh m⁻² yr⁻¹)  
- `co2_emissions` (kg CO₂ m⁻² yr⁻¹)  
- `final_energy_consumption` (kWh m⁻² yr⁻¹)  
- Service-specific energy & emissions for **heating, cooling, DHW, lighting**.

### 4 Building characteristics  
- `year_of_construction`, `cadastral_meters` (floor area)  
- `us_building` (residential / tertiary categories)  
- Average **U-values** for façades & windows + CTE regulatory limits.  
- Presence of **renewables & low-carbon tech** (`solar_photovoltaic`, `solar_thermal`, `geothermal_energy`, `electric_vehicle`, `district_network`, `biomass_system`).  

### 5 Retrofit metadata  
- `energy_rehabilitation` (Yes/No)  
- Free-text `rehabilitation_actions`.  

---

##  Typical Use-Cases  
1. **Spatial analytics** – map EPC ratings vs. socio-economic indicators at census-tract level.  
2. **Policy evaluation** – track retrofit rates before/after subsidy schemes.  
3. **Stock modelling** – create archetypes for building-energy simulation (TABULA, Hotmaps).  
4. **Machine-learning research** – predict EPC class from geometries, climate zone, and age.  
5. **Urban-planning dashboards** – identify high-priority renovation clusters.  

Check out the [Energy Efficiency Certification: Everything You Need to Know](https://tecno-consultor.com/en/energy-efficiency-certification/) on the common retrofit actions. 
