-- Define bin width and minimum and maximum assessed values
DECLARE bin_width NUMERIC DEFAULT 10000;
DECLARE min_assessed_value NUMERIC DEFAULT 0;
DECLARE max_assessed_value NUMERIC DEFAULT 5000000;
DECLARE upper_bound NUMERIC;
DECLARE lower_bound NUMERIC;
DECLARE property_count INT64;


-- Loop over the bins and count the number of properties in each bin
WHILE min_assessed_value < max_assessed_value DO
  SET upper_bound = min_assessed_value + bin_width;
  SET property_count = (
    SELECT COUNT(*)
    FROM core.opa_assessments
    WHERE market_value >= min_assessed_value
    AND market_value < upper_bound
    And year = 2023
  );
  INSERT INTO derived.tax_year_assessment_bins VALUES (
    2023,
    min_assessed_value,
    upper_bound,
    property_count
  );
  SET min_assessed_value = upper_bound;
END WHILE;