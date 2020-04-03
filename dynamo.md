#### Secondary index

	GlobalSecondaryIndex An index with a partition key and sort key that can be different from those on the table.
	LocalSecondaryIndex An index that has the same partition key as the table, but a different sort key.
	
#### Hints

	LocalSecondaryIndex must be created at the moment you create the table.

#### python and dynamodb

#### Dynamodb Stream

	Captures data modification events in DynamoDB tables.
	The data about these events appear in the stream in near real time,and in the order that the event occurred

	Each event is represented by a stream record, which contains the state of the item before and after inserts,updates and deletes.

	You can use stream together with lambda function to create triggers.
	These triggers execute automatically whenever an eventof interest appears in a stream.



