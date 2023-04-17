-- Define the bin width
DECLARE bin_width INT64 DEFAULT 10000;

CREATE TABLE derived.current_assessments_bins AS
WITH
  -- Calculate the bin index and lower_bound for each property
  property_bins AS (
    SELECT
      property_id,
      assessed_value,
      FLOOR(assessed_value / bin_width) * bin_width AS lower_bound
    FROM
      derived.current_assessments
  ),
  -- Count the number of properties in each bin and calculate the upper_bound
  bin_counts AS (
    SELECT
      lower_bound,
      lower_bound + bin_width - 1 AS upper_bound,
      COUNT(property_id) AS property_count
    FROM
      property_bins
    GROUP BY
      lower_bound
    ORDER BY
      lower_bound
  )
SELECT * FROM bin_counts;
