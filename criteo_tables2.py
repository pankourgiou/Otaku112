#x = "import os import sys from sqlalchemy import Column, String, Integer, BIGINT, Numeric, Date, DateTime"
#x1 = "sys.path.append('../') from helpers.database import db_connection as db lib_path = os.path.join(str(os.getenv(HOME)), 'python_lib', 'conf_fo') sys.path.append(lib_path) import global_configuration"
#x2 = "criteo_accounts=global_configuration.Criteo.accounts con_yml_dict = { db_user: global_configuration.DwhPsql.db_user db_passwd: global_configuration.DwhPsql.db_passwd, db_name: global_configuration.DwhPsql.db_name, db_host: global_configuration.DwhPsql.db_host, db_port: int(global_configuration.DwhPsql.db_port) } db_conn =db.DBConnection(con_yml_dict,global_configuration.Criteo.schema) session = db_conn.get_session() hash_id = db_conn.get_hash_id get_date = db_conn.get_date"
#x3 = "class CriteoCampaigns(db_conn.get_base()): __tablename__ = 'criteo_campaigns' def __init__(self, **kwargs): if 'id' not in kwargs:kwargs['id'] = hash_id(kwargs['campaign_id']) self.id = kwargs['id'] super(CriteoCampaigns, self).__init__(**kwargs) id = Column(String(32), primary_key=True) campaign_id = Column(Integer) campaign_name = Column(String(100)) campaign_status = Column(String(20)) country_code = Column(String(2)) currency_code = Column(String(3)) created_at = Column(DateTime(timezone=True), default=get_date()) updated_at = Column(DateTime(timezone=True), onupdate=get_date())"
#x4 = "class CriteoCampaignCosts(db_conn.get_base()): __tablename__ = 'criteo_campaign_costs' def __init__(self, **kwargs): if 'id' not in kwargs : kwargs['id'] = hash_id(kwargs['campaign_id'], kwargs['campaign_date']) self.id = kwargs['id'] super(CriteoCampaignCosts, self).__init__(**kwargs)"
#x5 = "id = Column(String(32), primary_key=True) campaign_id = Column(Integer) campaign_date = Column(Date) clicks = Column(Integer) impressions = Column(BIGINT) ctr = Column(Numeric(scale=2, precision=5, asdecimal=True)) rev_cpc = Column(Numeric(scale=2, precision=5, asdecimal=True)) ecpm = Column(Numeric(scale=2, precision=5, asdecimal=True)) cost = Column(Numeric(scale=2, precision=10, asdecimal=True)) sales = Column(Integer) conv_rate = Column(Numeric(scale=2, precision=10, asdecimal=True)) order_value = Column(Numeric(scale=2, precision=10, asdecimal=True)) sales_post_view = Column(Integer) conv_rate_post_view = Column(Numeric(scale=2, precision=10, asdecimal=True)) order_value_post_view = Column(Numeric(scale=2, precision=10, asdecimal=True)) cost_of_sale = Column(Numeric(scale=2, precision=10, asdecimal=True)) overall_competition_win = Column(Numeric(scale=2, precision=10, asdecimal=True)) cost_per_order = Column(Numeric(scale=2, precision=10, asdecimal=True)) created_at = Column(DateTime(timezone=True), default=get_date()) updated_at = Column(DateTime(timezone=True), onupdate=get_date())"

#print(bool(x))
#print(bool(x1))
#print(bool(x2))
#print(bool(x3))
#print(bool(x4))
#print(bool(x5))
