// Mirrors scripts/afano_data.py DIVISIONS. Keep in sync.
export type Division = {
  num: number;
  name: string;
  color: string;
  slug: string;
  subdomain: string;
  glyph: string;
  summary: string;
  businessUnits: { name: string; services: string[] }[];
};

export const DIVISIONS: Division[] = [
  { num: 1, name: "Financial Services & FinTech", color: "#0E3A5F", slug: "financial-services", subdomain: "financial", glyph: "coin",
    summary: "Multinational financial-services holding spanning banking, capital markets, insurance, payments and FinTech infrastructure.",
    businessUnits: [
      { name: "Banking & Lending", services: ["Commercial banking", "Microfinance", "Islamic finance (sukuk, murabaha)", "Trade finance"] },
      { name: "Insurance & Reinsurance", services: ["Life", "Property & casualty", "Reinsurance", "Captive insurance"] },
      { name: "Capital Markets", services: ["Investment banking", "Asset management", "Wealth management"] },
      { name: "FinTech & Payments", services: ["Digital wallets", "Cross-border payments", "Embedded finance"] },
    ] },
  { num: 2, name: "Energy & Natural Resources", color: "#1F6E3E", slug: "energy", subdomain: "energy", glyph: "flame",
    summary: "Integrated energy and resources platform across hydrocarbons, renewables, mining and the energy transition.",
    businessUnits: [
      { name: "Oil & Gas", services: ["Upstream", "Midstream", "Downstream marketing"] },
      { name: "Renewable Energy", services: ["Solar IPPs", "Wind", "Green hydrogen"] },
      { name: "Mining & Minerals", services: ["Industrial minerals", "Critical minerals (lithium, cobalt)", "Quarry"] },
      { name: "Utilities & Grid", services: ["Power distribution", "Smart-grid services"] },
    ] },
  { num: 3, name: "Technology & Digital", color: "#3B2E8C", slug: "technology", subdomain: "tech", glyph: "node",
    summary: "Technology platform spanning enterprise software, AI, cybersecurity and digital infrastructure.",
    businessUnits: [
      { name: "Cybersecurity", services: ["Managed detection & response", "GRC", "Offensive security"] },
      { name: "Telecommunications", services: ["Carrier services", "Internet service provision", "Tower infrastructure"] },
      { name: "AI & Data", services: ["AI platforms", "Data engineering", "Applied ML"] },
      { name: "Cloud & Digital Infrastructure", services: ["Cloud services", "Hosting", "Datacenter"] },
    ] },
  { num: 4, name: "Infrastructure & Real Estate", color: "#7C4A1E", slug: "infrastructure", subdomain: "infra", glyph: "pillar",
    summary: "Civil infrastructure, property development and real-estate asset management.",
    businessUnits: [
      { name: "Construction & Engineering", services: ["Heavy civil", "Building construction", "EPC contracting"] },
      { name: "Real Estate Development", services: ["Residential", "Commercial", "Mixed-use"] },
      { name: "Property Management & REIT", services: ["Asset management", "REIT structuring"] },
    ] },
  { num: 5, name: "Agriculture & Agribusiness", color: "#3F6B1B", slug: "agriculture", subdomain: "agri", glyph: "leaf",
    summary: "Farm-to-fork agribusiness covering production, processing and distribution.",
    businessUnits: [
      { name: "Crop Production", services: ["Grains", "Tubers", "Cash crops"] },
      { name: "Livestock & Aquaculture", services: ["Poultry", "Cattle", "Fish farming"] },
      { name: "Food Processing", services: ["FMCG manufacturing", "Cold-chain logistics"] },
    ] },
  { num: 6, name: "Healthcare & Life Sciences", color: "#B0364D", slug: "healthcare", subdomain: "health", glyph: "caduceus",
    summary: "Integrated healthcare platform from primary care to pharmaceuticals.",
    businessUnits: [
      { name: "Hospitals & Clinics", services: ["Acute care", "Specialty clinics", "Primary care"] },
      { name: "Pharmaceuticals", services: ["Manufacturing", "Distribution"] },
      { name: "Diagnostics & MedTech", services: ["Diagnostic imaging", "Laboratory services"] },
      { name: "Digital Health", services: ["Telehealth", "EMR/EHR"] },
    ] },
  { num: 7, name: "Tourism, Hospitality & Mobility", color: "#2E7CA8", slug: "mobility", subdomain: "voyage", glyph: "compass",
    summary: "Tourism, hospitality and mobility — air, ground and sea.",
    businessUnits: [
      { name: "Hospitality", services: ["Hotels", "Resorts", "F&B"] },
      { name: "Aviation", services: ["Charter operations", "MRO", "Ground handling"] },
      { name: "Maritime & Ports", services: ["Shipping", "Port operations", "Marine logistics"] },
      { name: "Ground Mobility", services: ["Ride-hailing", "Fleet", "Last-mile"] },
    ] },
  { num: 8, name: "Education & Workforce", color: "#8C5F1B", slug: "education", subdomain: "academy", glyph: "torch",
    summary: "Education, vocational training and workforce development.",
    businessUnits: [
      { name: "Academy (cybit360.com — live)", services: ["Cybersecurity training", "Tech bootcamps"] },
      { name: "K-12 & Higher Education", services: ["Schools", "Tertiary partnerships"] },
      { name: "Workforce Development", services: ["Apprenticeships", "Corporate L&D"] },
    ] },
  { num: 9, name: "Media & Entertainment", color: "#7B3FB3", slug: "media", subdomain: "media", glyph: "wave",
    summary: "Media, content and live entertainment.",
    businessUnits: [
      { name: "Production Studios", services: ["Film", "TV", "Streaming originals"] },
      { name: "Publishing", services: ["Book", "Digital media"] },
      { name: "Live Events", services: ["Festivals", "Conferences"] },
    ] },
  { num: 10, name: "Trade & Commerce", color: "#C56B1A", slug: "trade", subdomain: "trade", glyph: "ship",
    summary: "Trading, distribution, logistics and e-commerce — the keiretsu trading-house function.",
    businessUnits: [
      { name: "Commodity Trading", services: ["Soft commodities", "Hard commodities"] },
      { name: "Logistics & Freight", services: ["Freight forwarding", "Warehousing"] },
      { name: "E-Commerce & Retail", services: ["Marketplaces", "Direct-to-consumer"] },
    ] },
  { num: 11, name: "Government, Defense & Security", color: "#34495E", slug: "defense", subdomain: "civic", glyph: "shield",
    summary: "Government services, defense, security and sovereign technology.",
    businessUnits: [
      { name: "Government Advisory", services: ["Public-sector consulting", "Policy advisory"] },
      { name: "Defense & Security Services", services: ["Critical-infrastructure protection", "Cyber defense"] },
      { name: "Aerospace & Defense Manufacturing", services: ["UAV", "Sensors", "Satellite ground systems"] },
    ] },
  { num: 12, name: "Industrial Manufacturing", color: "#5A5A5A", slug: "industrial", subdomain: "forge", glyph: "gear",
    summary: "Heavy industry, advanced manufacturing and industrial services.",
    businessUnits: [
      { name: "Heavy Industry", services: ["Steel", "Cement", "Petrochemicals"] },
      { name: "Advanced Manufacturing", services: ["Precision components", "Additive manufacturing"] },
      { name: "Industrial Equipment", services: ["Equipment leasing", "Plant maintenance"] },
    ] },
  { num: 13, name: "Professional & Business Services", color: "#1F4F4F", slug: "professional", subdomain: "advisory", glyph: "bridge",
    summary: "Professional services — consulting, legal, accounting, HR and back-office.",
    businessUnits: [
      { name: "Management Consulting", services: ["Strategy", "Operations", "Digital transformation"] },
      { name: "Legal Services", services: ["Corporate", "IP", "Regulatory"] },
      { name: "Accounting, Tax & Audit", services: ["Statutory audit", "Tax advisory"] },
      { name: "HR & Talent", services: ["Executive search", "Outsourced HR"] },
    ] },
  { num: 14, name: "Social Impact & Development", color: "#A0552D", slug: "impact", subdomain: "impact", glyph: "hands",
    summary: "Social impact, philanthropy and sustainable development — the Group's giving and ESG-aligned investment arm.",
    businessUnits: [
      { name: "Foundation", services: ["Grant-making", "Scholarships", "Disaster response"] },
      { name: "Impact Investing", services: ["Blended finance", "Catalytic capital"] },
      { name: "Community Development", services: ["Local infrastructure", "Capacity building"] },
    ] },
  { num: 15, name: "Sports, Recreation & Youth", color: "#1F7A60", slug: "sports", subdomain: "arena", glyph: "star",
    summary: "Sports business, youth development and recreation infrastructure.",
    businessUnits: [
      { name: "Professional Teams", services: ["Football clubs", "Esports teams"] },
      { name: "Academy & Youth Development", services: ["Sports academies", "Youth pipelines"] },
      { name: "Venues & Recreation", services: ["Stadiums", "Recreation centers"] },
    ] },
];
