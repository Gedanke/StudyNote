?	:d?w_	@:d?w_	@!:d?w_	@	?S??????S?????!?S?????"e
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails$:d?w_	@???n???A'k?C4Z@Y5`??i??*	m?????I@2F
Iterator::ModelO???И?!?(??XG@)l#?	??1݋+?+.>@:Preprocessing2j
3Iterator::Model::ParallelMap::Zip[1]::ForeverRepeat???????!f%?	=@)EKO???1????f:@:Preprocessing2S
Iterator::Model::ParallelMap?R??%???!P?`{^?0@)?R??%???1P?`{^?0@:Preprocessing2d
-Iterator::Model::ParallelMap::Zip[0]::FlatMapƢ??dp??![???:3@)?????P}?1pdw??+@:Preprocessing2t
=Iterator::Model::ParallelMap::Zip[0]::FlatMap[0]::TensorSlice?Ŧ?B g?!?l?y?@)?Ŧ?B g?1?l?y?@:Preprocessing2X
!Iterator::Model::ParallelMap::Zip1???6T??!j?9?:?J@)??-Ye?1K????@:Preprocessing2v
?Iterator::Model::ParallelMap::Zip[1]::ForeverRepeat::FromTensor???}??V?!7t,??9@)???}??V?17t,??9@:Preprocessing:?
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
?Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
?Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
?Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
?Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)?
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysis?
device?Your program is NOT input-bound because only 1.3% of the total step time sampled is waiting for input. Therefore, you should focus on reducing other time.no*moderate2B10.6 % of the total step time sampled is spent on All Others time.#You may skip the rest of this page.B?
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown?
	???n??????n???!???n???      ??!       "      ??!       *      ??!       2	'k?C4Z@'k?C4Z@!'k?C4Z@:      ??!       B      ??!       J	5`??i??5`??i??!5`??i??R      ??!       Z	5`??i??5`??i??!5`??i??JCPU_ONLY2black"?
device?Your program is NOT input-bound because only 1.3% of the total step time sampled is waiting for input. Therefore, you should focus on reducing other time.b
`input_pipeline_analyzer (especially Section 3 for the breakdown of input operations on the Host)m
ktrace_viewer (look at the activities on the timeline of each Host Thread near the bottom of the trace view)"T
Rtensorflow_stats (identify the time-consuming operations executed on the CPU_ONLY)"Z
Xtrace_viewer (look at the activities on the timeline of each CPU_ONLY in the trace view)*y
w<a href="https://www.tensorflow.org/guide/data_performance" target="_blank">Better performance with the tf.data API</a>2?
=type.googleapis.com/tensorflow.profiler.GenericRecommendationR
nomoderate"B10.6 % of the total step time sampled is spent on All Others time.:
Refer to the TF2 Profiler FAQ2"CPU: 