from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from trails.models import Trail

@api_view(['GET', 'POST'])
def name(request, name):
    """
    Find all trails by a given name
    """
    if request.method == 'GET':
		if len(name) > 2:
			# TODO: Run query
		else:
			return Response('', status=status.HTTP_400_BAD_REQUEST)
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
