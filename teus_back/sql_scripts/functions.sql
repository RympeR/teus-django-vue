select 
	info_city.id "city_id", info_city.name "city name", 
	users_user.id "user_id", users_user.phone "user phone", 
	info_line.id "line id", info_line.name "line name",
	info_container.id "container id", info_container.name "container name",
	containers_userrequest.amount "amount",
	containers_userrequest.request_date "date"
	from containers_userrequest
join info_city on containers_userrequest.city_id = info_city.id
join users_user on containers_userrequest.user_id = users_user.id
join info_line on containers_userrequest.line_id = info_line.id
join info_container on containers_userrequest.container_id = info_container.id



select 
	info_city.id "city_id", info_city.name "city name", 
	users_user.id "user_id", users_user.phone "user phone", 
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