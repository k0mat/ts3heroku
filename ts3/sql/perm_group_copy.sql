insert into :table: (server_id, name, type) select :dest_server_id:, name, :dest_type: from :table: where server_id=:src_server_id: and type=:src_type: