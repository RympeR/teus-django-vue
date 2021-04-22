from .psycopg_sql import *


class UserFilter:

    def where_add(self, query):
        if 'where' not in query:
            query += '\nwhere'
        return query

    # TODO-- UPDATE METHOD
    def add_in_case(self, request, query, param_name, field_name):
        if request.query_params.get(param_name, None) not in ('empty', '', None):
            query = self.where_add(query)
            param = request.query_params[param_name]
            if query.split('\n')[-1].strip() != 'where':
                for value in param:
                    query += f"\nand {field_name} in '%{value}%'\n"
            else:
                for value in param:
                    query += f"\n{field_name} like '%{value}%'\n"
        return query

    def add_and_case(self, request, query, param_name, field_name, str_=True):
        if request.query_params.get(param_name, None) not in ('empty', '', None):
            query = self.where_add(query)
            param = request.query_params[param_name]
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
        if request.query_params.get(param_name, None) not in ('empty', '', None):
            query = self.where_add(query)
            param = request.query_params[param_name]
            param_end = request.query_params.get(param_end_name, None)
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

    def get_users(self, request, login, password):
        base_query = '''
            select * from users_user
                where is_admin = false
        '''
        try:
            query = base_query
            query = self.add_and_case(
                request, query, 'first_name', 'users_user.first_name')
            query = self.add_and_case(
                request, query,  'last_name', 'users_user.last_name')
            query = self.add_and_case(
                request, query, 'phone', 'users_user.phone')
            query += ';'
            print(query)
            result = execute_select_query(login, password, query)

        except Exception as e:
            print(e)
            print('failed')
            query = base_query + 'order by users_user.id DESC;'
            result = execute_select_query(login, password, query)
        return result

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
                containers_userproposition.end_date "end_date",
                containers_userproposition.status "status"
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
                request, query,  'user_phone', 'users_user.phone')
            query = self.add_and_case(
                request, query, 'line_name', 'info_line.name')
            query = self.add_and_case(
                request, query,  'container_name', 'info_container.name')
            query = self.add_and_case(
                request, query, 'amount', 'amount', str_=False)
            query = self.add_and_case(
                request, query, 'status', 'status', str_=False)
            query = self.add_between_case(
                request, query,  'request_date', 'request_end_date', 'containers_userproposition.start_date', str_=False)
            query = self.add_between_case(request, query, 'request_date',
                                          'request_end_date', 'containers_userproposition.end_date',  or_=True, str_=False)
            query += 'order by "date" desc, "end_date" desc;'
            print(query)
            result = execute_select_query(login, password, query)

        except Exception as e:
            print(e)
            print('failed')
            query = base_query + 'order by "date" desc;'
            result = execute_select_query(login, password, query)
        return result

    def get_requests(self, request, login, password):
        base_query = '''
              select
                containers_userrequest.id,
                 array_agg(info_city.name),
                users_user.id "user id", users_user.first_name "user name", users_user.phone "user phone",
                info_line.id "line id", info_line.name "line name",
                info_container.id "container id", info_container.name "container name",
                containers_userrequest.amount "amount",
                containers_userrequest.request_date "date",
                containers_userrequest.end_date "end date",
                containers_userrequest.status "status"
             from containers_userrequest
            join containers_userrequest_city on containers_userrequest.id = containers_userrequest_city.userrequest_id
            join info_city on containers_userrequest_city.city_id = info_city.id
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
                request, query,  'user_phone', 'users_user.phone')
            query = self.add_and_case(
                request, query, 'line_name', 'info_line.name')
            query = self.add_and_case(
                request, query,  'container_name', 'info_container.name')
            query = self.add_and_case(
                request, query, 'amount', 'amount', str_=False)
            query = self.add_and_case(
                request, query, 'status', 'status', str_=False)
            query = self.add_between_case(
                request, query,  'request_date', 'request_end_date', 'containers_userrequest.request_date', str_=False)
            query += '''
               group by 1,3,5,6,7,8,9,10,4
                order by "date", "end_date" desc;'''
            print(query)
            result = execute_select_query(login, password, query)

        except Exception as e:
            print(e)
            query = base_query + '''
                group by 1,3,5,6,7,8,9,10,4
                order by "date" desc, "end_date" desc;'''
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
                request, query,  'first_user_name', 'user1.first_name')
            query = self.add_and_case(
                request, query,  'first_user_phone', 'user1.phone')
            query = self.add_and_case(
                request, query,  'sec_user_name', 'user2.first_name')
            query = self.add_and_case(
                request, query,  'sec_user_phone', 'user2.phone')
            query = self.add_and_case(
                request, query, 'line_name', 'info_line.name')
            query = self.add_and_case(
                request, query,  'container_name', 'info_container.name')
            query = self.add_and_case(
                request, query, 'amount', 'amount', str_=False)
            query = self.add_between_case(
                request, query,  'handshake', 'handshake_end', 'containers_deal.handshake_time')
            query += 'order by containers_deal.handshake_time desc;'
            print(query)
            result = execute_select_query(login, password, query)

        except Exception as e:
            print(e)
            query = base_query + 'order by containers_deal.handshake_time desc;'
            result = execute_select_query(login, password, query)
        return result
