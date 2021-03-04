from .psycopg_sql import *
class UserFilter:

    

    def where_add(self, query):
        if 'where' not in query:
            query += '\nwhere'
        return query

    def add_and_case(self, request, query, param_name, field_name, str_=True):
        print(request.GET.get(param_name, None))
        if request.GET.get(param_name, None) not in ('empty', '', None):
            query = self.where_add(query)
            param = request.GET[param_name]
            if query.split('\n')[-1].strip() != 'where':
                if str_:
                    query += f"\nand {field_name} like '%{param}%'"
                else:
                    query += f"\nand {field_name}= {param}"
            else:
                if str_:
                    query += f"\n{field_name} like '%{param}%'"
                else:
                    query += f"\n{field_name}= {param}"
        return query

    def add_between_case(self, request, query, param_name, param_end_name, field_name, str_=True, or_=False):
        if request.GET.get(param_name, None) not in ('empty', '', None):
            query = self.where_add(query)
            param = request.GET[param_name]
            param_end = request.GET.get(param_end_name, None)
            if query.split('\n')[-1].strip() != 'where':
                if not or_:
                    if str_:
                        if param_end:
                            query += f"\nand {field_name} between '{param}' and '{param_end}'"
                        else:
                            query += f"\nand {field_name} >= '{param}'"
                    else:
                        if param_end:
                            query += f"\nand {field_name} between {param} and {param_end}"
                        else:
                            query += f"\nand {field_name} >= {param}"
                else:
                    if str_:
                        if param_end:
                            query += f"\nor {field_name} between '{param}' and '{param_end}'"
                        else:
                            query += f"\nor {field_name} >= '{param}'"
                    else:
                        if param_end:
                            query += f"\nor {field_name} between {param} and {param_end}"
                        else:
                            query += f"\nor {field_name} >= {param}"
            else:
                if str_:
                    if param_end:
                        query += f"\n {field_name} between '{param}' and '{param_end}'"
                    else:
                        query += f"\n {field_name} >= '{param}'"
                else:
                    if param_end:
                        query += f"\n {field_name} between {param} and {param_end}"
                    else:
                        query += f"\n {field_name} >= {param}"
        return query

    def get_propositions(self, request, login, password):
        base_query = '''
            select
                containers_userproposition.id,
                info_city.id "city_id", info_city.name "city name", 
                users_user.id "user_id", users_user.first_name "user name", users_user.phone "user phone", 
                info_line.id "line id", info_line.name "line name",
                info_container.id "container id", info_container.name "container name",
                containers_userproposition.amount "amount",
                containers_userproposition.start_date "date",
                containers_userproposition.end_date "end date"
                from containers_userproposition
            join info_city on containers_userproposition.city_id = info_city.id
            join users_user on containers_userproposition.user_id = users_user.id
            join info_line on containers_userproposition.line_id = info_line.id
            join info_container on containers_userproposition.container_id = info_container.id
        '''
        try:
            query = base_query
            query = self.add_and_case(
                request, query, 'city_name', 'info_city.name')
            query = self.add_and_case(
                request, query,  'user_name', 'users_user.first_name')
            query = self.add_and_case(
                request, query, 'line_name', 'info_line.name')
            query = self.add_and_case(
                request, query,  'container_name', 'info_container.name')
            query = self.add_and_case(
                request, query, 'amount', 'amount', str_=False)
            query = self.add_between_case(
                request, query,  'request_date', 'request_end_date', 'containers_userproposition.start_date')
            query = self.add_between_case(request, query, 'request_date',
                                          'request_end_date', 'containers_userproposition.end_date',  or_=True)
            query += ';'
            print(query)
            result = execute_select_query(login, password, query)

        except Exception as e:
            print(e)
            print('failed')
            query = base_query + ';'
            result = execute_select_query(login, password, query)
        return result

    def get_requests(self, request, login, password):
        base_query = '''
            select
                containers_userrequest.id,
                info_city.id "city id", info_city.name "city name", 
                users_user.id "user id", users_user.first_name "user name", users_user.phone "user phone", 
                info_line.id "line id", info_line.name "line name",
                info_container.id "container id", info_container.name "container name",
                containers_userrequest.amount "amount",
                containers_userrequest.request_date "date"
                from containers_userrequest
            join info_city on containers_userrequest.city_id = info_city.id
            join users_user on containers_userrequest.user_id = users_user.id
            join info_line on containers_userrequest.line_id = info_line.id
            join info_container on containers_userrequest.container_id = info_container.id  
        '''
        try:
            query = base_query
            query = self.add_and_case(
                request, query, 'city_name', 'info_city.name')
            query = self.add_and_case(
                request, query,  'user_name', 'users_user.first_name')
            query = self.add_and_case(
                request, query, 'line_name', 'info_line.name')
            query = self.add_and_case(
                request, query,  'container_name', 'info_container.name')
            query = self.add_and_case(
                request, query, 'amount', 'amount', str_=False)
            query = self.add_between_case(
                request, query,  'request_date', 'request_end_date', 'containers_userrequest.request_date')
            query += ';'
            print(query)
            result = execute_select_query(login, password, query)

        except Exception as e:
            print(e)
            query = base_query + ';'
            result = execute_select_query(login, password, query)
        return result

    def get_deals(self, request, login, password):
        base_query = '''
            select
                containers_deal.id,
                info_city.id "city_id", info_city.name "city name",
				user1.id "user1_id", user1.first_name "user1_name", user1.phone "user1 phone",
                user2.id "user2_id", user2.first_name "user2_name", user2.phone "user2 phone",
                info_line.id "line id", info_line.name "line name",
                info_container.id "container id", info_container.name "container name",
                containers_deal.amount "amount",
                containers_deal.handshake_time "handshake_time"
                from containers_deal
            join info_city on containers_deal.city_id = info_city.id
            join info_line on containers_deal.line_id = info_line.id
			join users_user as user2 on containers_deal.user_proposition_id = user2.id
            join users_user as user1 on containers_deal.user_request_id = user1.id
            join info_container on containers_deal.container_id = info_container.id
        '''
        try:
            query = base_query
            query = self.add_and_case(
                request, query, 'city_name', 'info_city.name')
            query = self.add_and_case(
                request, query,  'user1_phone', 'user1.phone')
            query = self.add_and_case(
                request, query,  'user1_name', 'user1.first_name')
            query = self.add_and_case(
                request, query,  'user2_phone', 'user2.phone')
            query = self.add_and_case(
                request, query,  'user2_name', 'user2.first_name')
            query = self.add_and_case(
                request, query, 'line_name', 'info_line.name')
            query = self.add_and_case(
                request, query,  'container_name', 'info_container.name')
            query = self.add_and_case(
                request, query, 'amount', 'amount', str_=False)
            query = self.add_between_case(
                request, query,  'handshake_time', 'handshake_end_time', 'containers_deal.handshake_time')
            query += ';'
            print(query)
            result = execute_select_query(login, password, query)

        except Exception as e:
            print(e)
            query = base_query + ';'
            result = execute_select_query(login, password, query)
        return result
