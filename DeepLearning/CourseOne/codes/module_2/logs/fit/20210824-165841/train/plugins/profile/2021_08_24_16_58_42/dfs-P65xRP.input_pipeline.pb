	?@j@?@j@!?@j@	WF?{???WF?{???!WF?{???"e
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails$?@j@&?R?o*??A<?y?9@Yi??r????*	C`??"KJ@2F
Iterator::Model?Z??Ù?!?񪿜?G@)&???J??1??%/A>@:Preprocessing2j
3Iterator::Model::ParallelMap::Zip[1]::ForeverRepeat??j?#???!n~?}+?;@)h??52??1Rī?a@9@:Preprocessing2S
Iterator::Model::ParallelMap,am?????!S\?Y
?1@),am?????1S\?Y
?1@:Preprocessing2d
-Iterator::Model::ParallelMap::Zip[0]::FlatMap6??
(??!R???4?2@)?LN?S{?1e\??_)@:Preprocessing2t
=Iterator::Model::ParallelMap::Zip[0]::FlatMap[0]::TensorSlice??u??i?!~D?C?@)??u??i?1~D?C?@:Preprocessing2X
!Iterator::Model::ParallelMap::ZipU?Y??!KU@cJ@)cAJh?1b{???@:Preprocessing2v
?Iterator::Model::ParallelMap::Zip[1]::ForeverRepeat::FromTensorN?E? V?!????On@)N?E? V?1????On@:Preprocessing:?
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
?Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
?Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
?Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
?Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)?
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysis?
device?Your program is NOT input-bound because only 1.2% of the total step time sampled is waiting for input. Therefore, you should focus on reducing other time.no*no#You may skip the rest of this page.B?
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown?
	&?R?o*??&?R?o*??!&?R?o*??      ??!       "      ??!       *      ??!       2	<?y?9@<?y?9@!<?y?9@:      ??!       B      ??!       J	i??r????i??r????!i??r????R      ??!       Z	i??r????i??r????!i??r????JCPU_ONLY