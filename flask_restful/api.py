from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

DrivingAgents = {
	'1':{'name': 'Mark', 'age': 25, 'spec': 'Paris'},
	'2':{'name': 'Jane', 'age': 31, 'spec': 'New york'}
	}

parser = reqparse.RequestParser()

class DrivingAgentsList(Resource):
	def get(self):
		return DrivingAgents
	def post(self):
		parser.add_argument("name")
		parser.add_argument("age")
		parser.add_argument("spec")
		args = parser.parse_args()
		agent_id = int(max(DrivingAgents.keys())) + 1
		agent_id = '%i' % agent_id
		
		DrivingAgents[agent_id] = {
			"name": args["name"],
			"age": args["age"],
			"spec": args["spec"],
			}
		return DrivingAgents[agent_id],201


class DrivingAgent(Resource):
	def get(self, agent_id):
		print("Agent Id: ",agent_id)
		if agent_id not in DrivingAgents:
			return "Not found", 404
		else:
			return DrivingAgents[agent_id],200
	def put(self, agent_id):
		parser.add_argument("name")
		parser.add_argument("age")
		parser.add_argument("spec")
		args = parser.parse_args()
		if agent_id not in DrivingAgents:
			return "Not found", 404
		else:
			driving_agent = DrivingAgents[agent_id]
			driving_agent["name"] = args["name"] if args["name"] is not None else driving_agent["name"]
			driving_agent["age"]  = args["age"] if args["age"] is not None else driving_agent["age"]
			driving_agent["spec"] = args["spec"] if args["spec"] is not None else driving_agent["spec"]
			# DrivingAgents[agent_id] = driving_agent
			return DrivingAgents[agent_id], 200
	def delete(self, agent_id):
		if agent_id not in DrivingAgents:
			return "Not found", 404
		else:
			del DrivingAgents[agent_id]
			return 'Removed', 204


api.add_resource(DrivingAgentsList, '/drivingagents/')
api.add_resource(DrivingAgent,'/drivingagents/<agent_id>')

if __name__ == "__main__":
    app.run(debug=True)