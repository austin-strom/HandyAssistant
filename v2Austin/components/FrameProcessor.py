# import com.google.mediapipe.framework.Graph;
# import com.google.mediapipe.framework.GraphService;
# import com.google.mediapipe.framework.MediaPipeException;
# import com.google.mediapipe.framework.Packet;
# import com.google.mediapipe.framework.PacketCallback;
# import com.google.mediapipe.framework.PacketGetter;
# import com.google.mediapipe.framework.SurfaceOutput;
# import com.google.mediapipe.framework.TextureFrame;
from v2Austin.components.Graph import Graph


class FrameProcessor:

    def __init__(self, graph_name, input_stream, output_stream):

        self.graph_name = graph_name
        self.input_stream = input_stream
        self.output_stream = output_stream

        graph = Graph()

        # Load binary graph
        graph.load_binary_graph(graph_name)
