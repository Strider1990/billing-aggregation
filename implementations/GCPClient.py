from pandas.core.frame import DataFrame
from google.cloud import bigquery
from google.oauth2.service_account import Credentials
from interfaces import (
	DataTransform,
	PlatformClient
)

class GCPClient(PlatformClient, DataTransform):
	def __init__(self,
		service_account_file: str = None,
		service_account_info: str = None,
		project_id: str = None,
		dataset_id: str = None,
		table_id: str = None) -> None:

		super().__init__()
		credentials = None
		self.project_id = project_id
		self.dataset_id = dataset_id
		self.table_id = table_id
		if service_account_file:
			credentials = Credentials.from_service_account_file(service_account_file)
		if service_account_info:
			credentials = Credentials.from_service_account_info(service_account_info)

		if credentials:
			self.client = bigquery.Client(credentials=credentials, project=project_id)
		else:
			self.client = bigquery.Client(project=project_id)

	def get_platform_data(self, query: str) -> DataFrame:
		query_job = self.client.query(
			query=query,
		)

		return query_job.to_dataframe()

	def transform_data(self, df: DataFrame) -> DataFrame:
		pass