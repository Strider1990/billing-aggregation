from pandas.core.frame import DataFrame
from implementations.GCPClient import GCPClient
from interfaces.DataTransform import DataTransform
from interfaces.PlatformClient import PlatformClient
from dotenv import load_dotenv
import os

def get_data(client: PlatformClient, query: str) -> DataFrame:
	return client.get_platform_data(query=query)

def transform_data(client: DataTransform, df: DataFrame) -> DataFrame:
	return client.transform_data(df=df)

def main() -> None:
	load_dotenv()

	SA_FILE = os.environ["GCP_FILE"]
	QUERY = os.environ["GCP_QUERY"]
	clients = []
	clients.append(GCPClient(service_account_file=SA_FILE))
	df = None

	for client in clients:
		df = get_data(client, QUERY)
		transformed_df = transform_data(client, df)

if __name__=="__main__":
	main()