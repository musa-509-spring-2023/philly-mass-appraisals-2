CREATE OR REPLACE EXTERNAL TABLE `source.opa_assessments` (
    `property_id` STRING,
    `parcel_number` STRING,
    `year` INTEGER,
    `market_value` NUMERIC,
    `taxable_land` NUMERIC,
    `taxable_building` NUMERIC,
    `exempt_land` NUMERIC,
    `exempt_building` NUMERIC
)
OPTIONS (
    uris = ['gs://musa509s23_team02_prepared_data/opa_assessments/data.jsonl'],
    format = 'JSON'
)