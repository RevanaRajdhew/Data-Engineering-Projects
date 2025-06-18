import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node tracks
tracks_node1750169255574 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://proj-spotify-revanarajdhew/staging/track.csv"], "recurse": True}, transformation_ctx="tracks_node1750169255574")

# Script generated for node albums
albums_node1750169255087 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://proj-spotify-revanarajdhew/staging/albums.csv"], "recurse": True}, transformation_ctx="albums_node1750169255087")

# Script generated for node artists
artists_node1750169254538 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://proj-spotify-revanarajdhew/staging/artists.csv"], "recurse": True}, transformation_ctx="artists_node1750169254538")

# Script generated for node Join Artist & Album
JoinArtistAlbum_node1750169315426 = Join.apply(frame1=albums_node1750169255087, frame2=artists_node1750169254538, keys1=["artist_id"], keys2=["id"], transformation_ctx="JoinArtistAlbum_node1750169315426")

# Script generated for node Join with tracks
Joinwithtracks_node1750169416551 = Join.apply(frame1=tracks_node1750169255574, frame2=JoinArtistAlbum_node1750169315426, keys1=["track_id"], keys2=["track_id"], transformation_ctx="Joinwithtracks_node1750169416551")

# Script generated for node Drop Fields
DropFields_node1750169467151 = DropFields.apply(frame=Joinwithtracks_node1750169416551, paths=["`.track_id`", "id"], transformation_ctx="DropFields_node1750169467151")

# Script generated for node Destination
EvaluateDataQuality().process_rows(frame=DropFields_node1750169467151, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1750168719767", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
Destination_node1750169482915 = glueContext.write_dynamic_frame.from_options(frame=DropFields_node1750169467151, connection_type="s3", format="glueparquet", connection_options={"path": "s3://proj-spotify-revanarajdhew/datawarehouse/", "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="Destination_node1750169482915")

job.commit()